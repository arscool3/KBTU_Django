from fastapi import FastAPI, Depends

app = FastAPI()


####################################
def get_info():
    backend = {"name": "django backend"}
    return backend


#####################################

def get_order(backend: dict = Depends(get_info())):
    return backend.get("order")


@app.get("/order")
async def get_order(order: str = Depends(get_order)):
    return order


######################################
def get_account(backend: dict = Depends(get_info)):
    return backend.get("account")


@app.get("/account")
async def get_account(account: str = Depends(get_account)):
    return account
###############################################