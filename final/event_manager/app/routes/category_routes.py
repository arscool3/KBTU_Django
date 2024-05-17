from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import CategoryCreate, Category, CategoryUpdate
from models.models import Category as  DBCategory
from database.database import get_db
from crud.crud import( 
    get_by_id,
    get_all,
    create,
    update,
    delete
    )


router = APIRouter(prefix="/api/categories", tags=["categories"])

@router.post("/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create(db, DBCategory, category)

@router.get("/{category_id}", response_model=Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    db_category = get_by_id(db,DBCategory, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.put("/{category_id}", response_model=Category)
def update_existing_category(category_id: int, category_update: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = update(db,DBCategory, category_id, category_update)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_id}", response_model=Category)
def delete_existing_category(category_id: int, db: Session = Depends(get_db)):
    db_category = delete(db,DBCategory, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
