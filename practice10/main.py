from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
import schemas as sch
import database as db
import models as mdl
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import session
app = FastAPI()

def get_db():
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        session.close()


@app.post("/categories")
def add_category(category: sch.Category, session: Session = Depends(get_db)) -> str:
    session.add(mdl.Category(**category.model_dump()))
    return "Category was added"

@app.get("/categories/add")
def get_category_list(session: Session = Depends(get_db)):
    db_categories = session.query(mdl.Category).all()
    return [sch.Category.model_validate(category) for category in db_categories]


@app.post("/products")
def add_product(product: sch.Product, session: Session = Depends(get_db)) -> str:
    session.add(mdl.Product(**product.model_dump()))
    return "Products was added"

@app.get("/products/{category_id}")
def get_products_by_category(category_id: int, session = Depends(get_db)):
    db_products = session.query(mdl.Product).filter(
                        mdl.Product.category_id == category_id
                        ).all()
    return [sch.Product.model_validate(product) for product in db_products]


@app.get("/product/{product_id}")
def get_product_details(product_id: int, session: Session = Depends(get_db)):
    db_product = session.query(mdl.Product).filter(mdl.Product.id == product_id).first()
    return sch.Product.model_validate(db_product)

@app.post("/user")
def create_user(user: sch.User, session: Session = Depends(get_db)) -> str:
    session.add(mdl.User(**user.model_dump()))
    return "User was added"

@app.get("/users")
def get_users(session: Session = Depends(get_db)):
    db_users = session.execute(select(mdl.User)).scalars().all()
    return [sch.User.model_validate(user) for user in db_users]

@app.get("/user/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_db)):
    db_user = session.query(mdl.User).filter(mdl.User.id == user_id).first()
    return sch.User.model_validate(db_user)

@app.post("/createcart")
def create_Cart_for_Customer(cart: sch.Cart, session: Session = Depends(get_db)) -> str:
    session.add(mdl.Cart(**cart.model_dump()))
    return "Cart was added"

@app.post("/addtocart")
def add_to_cart(cartitem: sch.CartItem, session: Session = Depends(get_db)) -> str:
    session.add(mdl.CartItem(**cartitem.model_dump()))
    return "add success"

@app.get("/cartitems")
def get_cartitems(session: Session = Depends(get_db)):
    db_cartitems = session.execute(select(mdl.CartItem)).scalars().all()
    cartitems = [sch.CartItem.model_validate(cartitem) for cartitem in db_cartitems]
    return cartitems

@app.get("/cartitems/{customer_id}")
def get_cartitems_for_customer(customer_id: int, session: Session = Depends(get_db)):
    customer = session.query(mdl.Customer).filter(mdl.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    cartitems = session.query(mdl.CartItem).join(mdl.Cart).filter(mdl.Cart.customer_id == customer_id).all()

    validated_cartitems = [sch.CartItem.model_validate(cartitem) for cartitem in cartitems]
    return validated_cartitems  

@app.post("/store")
def create_store(store: sch.Store, session: Session = Depends(get_db)):
    session.add(mdl.Store(**store.model_dump()))
    return "Store created succesfull"

@app.get("/stores")
def get_store_list(session: Session = Depends(get_db)):
    db_stores = session.query(mdl.Store).all()
    return [sch.Store.model_validate(store) for store in db_stores]



@app.get("/stores/{store_id}")
def get_store_details(store_id: int, session: Session = Depends(get_db)):
    db_store = session.query(mdl.Store).filter(mdl.Store.id == store_id).first()

    if not db_store:
        raise HTTPException(status_code=404, detail="Store not found")

    return sch.Store.model_validate(db_store)

@app.post("/store/{store_id}/add")
def add_product_to_store(store_id: int, product_id: int, session: Session = Depends(get_db)):
    store = session.query(mdl.Store).filter(mdl.Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    product = session.query(mdl.Product).filter(mdl.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = session.query(mdl.StoreItem).filter(
        mdl.StoreItem.store_id == store_id, mdl.StoreItem.product_id == product_id
    ).first()

    if existing_item:
        return {"message": "Product already exists in the store."}
    else:
        new_item = mdl.StoreItem(store_id=store_id, product_id=product_id)
        session.add(new_item)
        return {"message": "Product successfully added to the store"}
    
@app.get("/store/{store_id}/products")
def get_store_products(store_id: int, session: Session = Depends(get_db)):
    store_items = session.query(mdl.StoreItem).filter(mdl.StoreItem.store_id == store_id).all()
    return [sch.StoreItem.model_validate(items) for items in store_items]