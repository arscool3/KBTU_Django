from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from auth.auth import create_access_token
from database import models
from database.db import get_db
import entity
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import auth
from . import crud
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

router = APIRouter()

# Authentication
@router.post("/login", response_model=entity.Token)
def login(details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == details.username).first()

    if not user or details.password != user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username or password")
    
    access_token = create_access_token(data={"username": user.username, "user_id": user.user_id})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=entity.User)
def register_user(user: entity.User, db: Session = Depends(get_db)):

    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    last_user = db.query(models.User).order_by(models.User.user_id.desc()).first()
    next_user_id = (last_user.user_id + 1) if last_user else 1

    new_user = models.User(user_id=next_user_id, username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    
@router.get("/me")
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user



# CRUD - Product
@router.post("/products", response_model=entity.Product)
def create_product(product_data: entity.Product, db: Session = Depends(get_db)):
    return crud.create(db=db, model_class=models.Product, model=product_data)

@router.get("/products/{product_id}", response_model=entity.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get(db=db, model_class=models.Product, model_id=product_id)
    
@router.put("/products/{product_id}", response_model=entity.Product)
def update_product(product_id: int, product_data: entity.ProductUpdate, db: Session = Depends(get_db)):
    return crud.update(db=db, model_class=models.Product, model_id=product_id, model_data=product_data)

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, model_class=models.Product, model_id=product_id)


# CRUD - Brand
@router.post("/brands", response_model=entity.Brand)
def create_brand(brand_data:entity.Brand, db: Session = Depends(get_db)):
    return crud.create(db=db, model_class=models.Brand, model=brand_data)

@router.get("/brands/{brand_id}", response_model=entity.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    return crud.get(db=db, model_class=models.Brand, model_id=brand_id)

@router.put("/brands/{brand_id}", response_model=entity.Brand)
def update_brand(brand_id: int, brand_data: entity.Brand, db: Session = Depends(get_db)):
    return crud.update(db=db, model_class=models.Brand, model_id=brand_id, model_data=brand_data)

@router.delete("/brands/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, model_class=models.Brand, model_id=brand_id)

# CRUD - Category
@router.post("/categories", response_model=entity.Category)
def create_category(category_data:entity.Category, db: Session = Depends(get_db)):
    return crud.create(db=db, model_class=models.Category, model=category_data)

@router.get("/categories/{category_id}", response_model=entity.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get(db=db, model_class=models.Category, model_id=category_id)

@router.put("/categories/{category_id}", response_model=entity.Category)
def update_category(category_id: int, category_data: entity.Category, db: Session = Depends(get_db)):
    return crud.update(db=db, model_class=models.Category, model_id=category_id, model_data=category_data)

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, model_class=models.Category, model_id=category_id)


# CRUD - Order
@router.post("/orders", response_model=entity.Order)
def create_order(order_data:entity.Order, db: Session = Depends(get_db)):
    return crud.create(db=db, model_class=models.Order, model=order_data)

@router.get("/orders/{order_id}", response_model=entity.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get(db=db, model_class=models.Order, model_id=order_id)

@router.put("/orders/{order_id}", response_model=entity.Order)
def update_order(order_id: int, order_data: entity.Order, db: Session = Depends(get_db)):
    return crud.update(db=db, model_class=models.Order, model_id=order_id, model_data=order_data)

@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, model_class=models.Order, model_id=order_id)

# CRUD - Review
@router.post("/reviews", response_model=entity.Review)
def create_review(review_data:entity.Review, db: Session = Depends(get_db)):
    return crud.create(db=db, model_class=models.Review, model=review_data)

@router.get("/reviews/{review_id}", response_model=entity.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return crud.get(db=db, model_class=models.Review, model_id=review_id)

@router.delete("/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, model_class=models.Review, model_id=review_id)