from sqlalchemy.orm import Session
from models import User, Post, Comment


def create_user(db: Session, username: str, email: str):
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_post(db: Session, title: str, content: str, author_id: int):
    db_post = Post(title=title, content=content, author_id=author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_comment(db: Session, text: str, post_id: int):
    db_comment = Comment(text=text, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()


def get_users(db: Session):
    return db.query(User).all()


def get_posts(db: Session):
    return db.query(Post).all()


def get_comments(db: Session):
    return db.query(Comment).all()
