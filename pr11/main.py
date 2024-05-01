from fastapi import FastAPI, Depends, HTTPException, WebSocket
from sqlalchemy import create_engine, Integer, Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, relationship, Session


app = FastAPI()

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)


class ToDoItem(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    done = Column(Boolean, index=True)


class ToDoList(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = relationship("User", back_populates="ToDoList")
    tasks: Mapped[list[ToDoItem]] = relationship("ToDoItem", back_populates="ToDoLists")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/tasks")
def get_tasks(db: Session = Depends()):
    tasks = db.query(ToDoList).all()
    return tasks


@app.post("/tasks/{task_id}")
def create_task(task: ToDoItem, db: Session = Depends(get_db)):
    todo = ToDoItem(**task.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.post("/todolist/")
def create_todolist(todo_list: ToDoList, db: Session = Depends(get_db)):
    db_todolist = ToDoList(**todo_list.dict())
    db.add(db_todolist)
    db.commit()
    db.refresh(db_todolist)
    return db_todolist


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except Exception as e:
        print(e)
    finally:
        await websocket.close()