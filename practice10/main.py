from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.templating import Jinja2Templates
from model import User, Item, Order

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DATABASE_URL = "postgresql://postgres:12345@localhost/postgres2"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.get("/users/", response_class=HTMLResponse)
async def user_list(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return templates.TemplateResponse("user_list.html", {"request": request, "users": users})


@app.get("/users/create/", response_class=HTMLResponse)
async def user_create(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})


@app.get("/users/{user_id}/update/", response_class=HTMLResponse)
async def user_update(request: Request, user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("user_update.html", {"request": request, "user": user})


@app.get("/users/{user_id}/delete/", response_class=HTMLResponse)
async def user_delete(request: Request, user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user:
        return templates.TemplateResponse("user_delete.html", {"request": request, "user": user})
    else:
        return "User not found", 404


# Define routes for item management
@app.get("/items/", response_class=HTMLResponse)
async def item_list(request: Request):
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return templates.TemplateResponse("item_list.html", {"request": request, "items": items})


@app.get("/items/create/", response_class=HTMLResponse)
async def item_create(request: Request):
    return templates.TemplateResponse("item_create.html", {"request": request})


# Define routes for order management
@app.get("/orders/", response_class=HTMLResponse)
async def order_list(request: Request):
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return templates.TemplateResponse("order_list.html", {"request": request, "orders": orders})


@app.get("/orders/create/", response_class=HTMLResponse)
async def order_create(request: Request):
    return templates.TemplateResponse("order_create.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
