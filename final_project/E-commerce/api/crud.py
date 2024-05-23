from sqlalchemy.orm import Session
from fastapi import status, HTTPException

from tasks import send_order_confirmation

def create(db: Session, model_class, model: dict):
    attribute_name = f"{model_class.__name__.lower()}_id"

    if model_class.__name__ != 'Order' and model_class.__name__ != 'Review':
        if db.query(model_class).filter(model_class.name == model.name).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{model_class.__name__} already exists")

    last = db.query(model_class).order_by(getattr(model_class, attribute_name).desc()).first()
    next_id = (getattr(last, attribute_name) + 1) if last else 1

    model_instance = model_class(**model.__dict__) 
    setattr(model_instance, attribute_name, next_id)

    if model_class.__name__ == 'Order':
        send_order_confirmation.send(model_instance.user_id, model_instance.order_id)

    db.add(model_instance)
    db.commit()
    db.refresh(model_instance)
    return model_instance

def get(db: Session, model_class, model_id: int):
    attribute_name = f"{model_class.__name__.lower()}_id"
    model = db.query(model_class).filter(getattr(model_class, attribute_name) == model_id).first()

    if model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return model

def update(db: Session, model_class, model_id: int, model_data: dict):
    attribute_name = f"{model_class.__name__.lower()}_id"
    model = db.query(model_class).filter(getattr(model_class, attribute_name) == model_id).first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    
    if model_class.__name__ != 'Order':
        if model_data.name:
            model.name = model_data.name
    else:
        model.status = model_data.status
        if model_data.user_id:
            model.user_id = model_data.user_id
        elif model_data.product_id:
            model.product_id = model_data.product_id

    if model_class.__name__ == 'Product':
        if model_data.description:
            model.description = model_data.description

    db.commit()
    db.refresh(model)
   
    return model

def delete(db: Session, model_class, model_id: int):
    attribute_name = f"{model_class.__name__.lower()}_id"
    model = db.query(model_class).filter(getattr(model_class, attribute_name) == model_id).first()
    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    db.delete(model)
    db.commit()
    return {"message": "Deleted successfully!"}
