from fastapi import FastAPI, Depends, HTTPException, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI()

def create_homepage():
    html_content = """
    <html>
        <head>
            <title>FastAPI Application</title>
        </head>
        <body>
            <h1>Welcome to the FastAPI application!</h1>
            <h2>Create an Item</h2>
            <form action="/items/" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="description">Description:</label>
                <input type="text" id="description" name="description"><br><br>
                <label for="price">Price:</label>
                <input type="text" id="price" name="price"><br><br>
                <label for="tax">Tax:</label>
                <input type="text" id="tax" name="tax"><br><br>
                <input type="submit" value="Submit">
            </form>
            
            <h2>Get User Token</h2>
            <form action="/users/" method="get">
                <label for="token">Token:</label>
                <input type="text" id="token" name="token"><br><br>
                <input type="submit" value="Submit">
            </form>

            <h2>Admin Access</h2>
            <form action="/admin/" method="get">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    return html_content

@app.get("/", response_class=HTMLResponse)
def read_root():
    return create_homepage()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

def calculate_tax(price: float) -> float:
    return price * 0.05

@app.post("/items/")
async def create_item(name: str = Form(...), description: Optional[str] = Form(None), 
                      price: float = Form(...), tax: Optional[float] = Form(None)):
    tax_value = calculate_tax(price) if tax is None else tax
    item_price_with_tax = price + tax_value
    return {"name": name, "price_with_tax": item_price_with_tax}


def get_query_token(token: str):
    if token != "togzhan":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return token

@app.get("/users/")
async def read_users(token: str = Depends(get_query_token)):
    return {"token": token}

def validate_admin_user(username: str):
    if username != "admin":
        raise HTTPException(status_code=401, detail="Not allowed")
    return username

@app.get("/admin/")
async def get_admin(username: str = Depends(validate_admin_user)):
    return {"username": username}
