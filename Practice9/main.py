from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Пример 1: через callable, в данном случае коннекшн с БД
def get_db_conn():
    return "DB Connection"

@app.get("/first/")
async def first(db: str = Depends(get_db_conn)):
    return {"database": db}


# Пример 2: Тоже самое только теперь мы еще чо-то получаем(параметр)
def getChoTo(choto: str):
    if choto != "choto":
        raise HTTPException(status_code=400, detail="Bad_request")
    return choto

@app.get("/second/")
async def second(choto: str = Depends(getChoTo)):
    return {"message": f"Bad_request: {choto}"}


# Пример 3: Класс
class Klassno:
    def __init__(self, choto: str):
        self.choto = choto

    def delaiChoTo(self):
        if self.choto != "choto":
            raise HTTPException(status_code=400, detail="Bad_request")
        return "Bad_request"

@app.get("/third/")
async def third(choto: Klassno = Depends()):
    return {"message": choto.delaiChoTo()}