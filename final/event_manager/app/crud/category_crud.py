# from sqlalchemy.orm import Session
# from models.models import Category as DBCategory
# from schemas.schemas import CategoryCreate, CategoryUpdate

# def create_category(db: Session, category: CategoryCreate):
#     db_category = DBCategory(**category.dict())
#     db.add(db_category)
#     db.commit()
#     db.refresh(db_category)
#     return db_category

# def get_category(db: Session, category_id: int):
#     return db.query(DBCategory).filter(DBCategory.id == category_id).first()

# def update_category(db: Session, category_id: int, category_update: CategoryUpdate):
#     db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
#     if db_category:
#         for attr, value in category_update.dict(exclude_unset=True).items():
#             setattr(db_category, attr, value)
#         db.commit()
#         db.refresh(db_category)
#     return db_category

# def delete_category(db: Session, category_id: int):
#     db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
#     if db_category:
#         db.delete(db_category)
#         db.commit()
#     return db_category
