from sqlalchemy.orm import Session
from models import Comment

def create_comment(db: Session, text: str, user_id: int, paper_id: int):
    comment = Comment(text=text, user_id=user_id, paper_id=paper_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def update_comment(db: Session, comment_id: int, text: str):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        comment.text = text
        db.commit()
        db.refresh(comment)
        return comment
    return None

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return True
    return False

