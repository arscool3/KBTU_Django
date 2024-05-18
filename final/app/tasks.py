import random
import dramatiq
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
import redis
from sqlalchemy.orm import Session

import models
from db import SessionLocal
import logging

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
redis_client = redis.Redis(host="localhost", port=6379, db=0)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@dramatiq.actor
def activate_user(user_id, code, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    value = redis_client.get(user.username)
    verification_code = value.decode("utf-8")
    logger.debug(f"value:{verification_code}{code}{user.username}")
    if verification_code == code:
        try:
            user.is_active = True
            db.add(user)
            db.commit()
            logger.info(f"User {user.username} activated successfully")
            return {"message": "User activated successfully"}
        except Exception as e:
            db.rollback()
            logger.error(f"Error activating user {user.username}: {str(e)}")
            return {"error": "Internal server error"}
    else:
        return {"error": "activation code not found"}


@dramatiq.actor
def send_activate_number(username):
    random_number = random.randint(1000, 9999)
    redis_client.set(username, random_number)


@dramatiq.actor
def get_activation_code(username):
    code = redis_client.get(username)
    verification_code = code.decode("utf-8")
    return verification_code
