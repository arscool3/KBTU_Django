from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, Boolean, Time, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base, sessionmaker
import dramatiq
from datetime import datetime, timedelta

Base = declarative_base()

class DaysOfWeek(Base):
    __tablename__ = 'main_days_of_week'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    day = Column(String(20), nullable=False)

class FlightFact(Base):
    __tablename__ = 'main_flight_fact'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    flight_code = Column(String(10))
    dept_time = Column(Time)
    arr_time = Column(Time)
    diff_days = Column(Integer)

class FlightDim(Base):
    __tablename__ = 'main_flight_dim'
    __table_args__ = {'schema': 'main'}

    flight_id = Column(Integer, primary_key=True)
    flight_code_id = Column(Integer)
    flight_date = Column(Date)
    is_sale_open = Column(Boolean)

# Define the junction table explicitly
class Flight_fact_Flight_days(Base):
    __tablename__ = 'main_flight_fact_flight_days'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    flight_fact_id = Column(Integer)
    days_of_week_id = Column(Integer)


database_url = 'sqlite:////Users/raiymbekovdaniyar/Projects/KBTU_Django/Midterm/db.sqlite3'
engine = create_engine(database_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@dramatiq.actor
def generate_flights_for_next_month_async(flight_code_id):
    session = Session()
    try:
        flight_days_query = session.query(Flight_fact_Flight_days.days_of_week_id).filter_by(
            flight_fact_id=flight_code_id)
        flight_days_list = [day_id for (day_id,) in flight_days_query]

        last_date_query = session.query(FlightDim).filter_by(flight_code_id=flight_code_id).order_by(
            FlightDim.flight_date.desc()).first()
        last_date = last_date_query.flight_date if last_date_query else datetime.now().date()

        first_day_next_month = (last_date.replace(day=1) + timedelta(days=32)).replace(day=1)
        last_day_next_month = (first_day_next_month + timedelta(days=32)).replace(day=1) + timedelta(days=-1)

        next_month_dates = [first_day_next_month + timedelta(days=i) for i in
                            range((last_day_next_month - first_day_next_month).days + 1)]

        for date in next_month_dates:
            if date.weekday() + 1 in flight_days_list:
                new_flight = FlightDim(flight_code_id=flight_code_id, flight_date=date, is_sale_open=False)
                session.add(new_flight)

        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Error generating flights: {e}')
    finally:
        session.close()
