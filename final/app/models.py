from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from app.db import Base
from datetime import datetime

paper_field = Table(
    'paper_field', Base.metadata,
    Column('paper_id', Integer, ForeignKey('papers.id')),
    Column('field_id', Integer, ForeignKey('fields.id'))
)

paper_tag = Table(
    'paper_tag', Base.metadata,
    Column('paper_id', Integer, ForeignKey('papers.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    papers = relationship("Paper", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    favorites = relationship("Favorite", back_populates="user")

class Paper(Base):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    abstract = Column(Text, nullable=False)
    file_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="papers")
    fields = relationship("Field", secondary=paper_field, back_populates="papers")
    tags = relationship("Tag", secondary=paper_tag, back_populates="papers")
    comments = relationship("Comment", back_populates="paper")
    favorites = relationship("Favorite", back_populates="paper")

class Field(Base):
    __tablename__ = 'fields'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    papers = relationship("Paper", secondary=paper_field, back_populates="fields")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    papers = relationship("Paper", secondary=paper_tag, back_populates="tags")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    paper_id = Column(Integer, ForeignKey('papers.id'))

    author = relationship("User", back_populates="comments")
    paper = relationship("Paper", back_populates="comments")

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    paper_id = Column(Integer, ForeignKey('papers.id'))

    user = relationship("User", back_populates="favorites")
    paper = relationship("Paper", back_populates="favorites")

