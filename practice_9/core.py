from fastapi import FastAPI, Depends

app = FastAPI()

# Example 1
def get_token():
    return "FakeToken"

@app.get("/items/")
async def read_items(token: str = Depends(get_token)):
    return {"token": token}


# Example 2
main_fruits_list = ["Apple"]

def call_main_fruits():
    return main_fruits_list

@app.get("/fruitss/")
def test_main_fruits(fruit:str, list = Depends(call_main_fruits)):
    list.append(fruit)
    print(list)
    return {"message":f"Added fruit {fruit} in the list!"}


#Example 3
async def sub_dependency_price(price: int):
    if price == 0:
        return 50
    else:
        return price

async def dependency_fruits(fruit: str, price: int = Depends(sub_dependency_price)):
    return {"Fruit": fruit, "Price": price}

@app.get("/fruits")
async def fetch_authors(fruits_list: dict = Depends(dependency_fruits)):
    return fruits_list

#DI is a technique to enhance code reusability 
#and facilitate the decoupling of a class from its dependencies.