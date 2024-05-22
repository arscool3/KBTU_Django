from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")
