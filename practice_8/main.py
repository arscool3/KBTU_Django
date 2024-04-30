from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

shops = []
products = []

class Paper(BaseModel):
    name: str
    author: str

class Category(BaseModel):
    name: str
    paper_id: int

papers = []

categories = []

@app.post("/papers/")
async def create_paper(paper: Paper):
    papers.append(paper)
    return {"message": "Paper created successfully"}

@app.get("/papers/", response_model=List[Paper])
async def get_papers():
    return papers

@app.get("/papers/{index}", response_model=Paper)
async def get_paper_by_index(index: int):
    try:
        return papers[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Paper not found")

@app.put("/papers/{index}")
async def update_paper(index: int, paper: Paper):
    try:
        papers[index] = paper
        return {"message": "Paper updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Paper not found")

@app.delete("/papers/{index}")
async def delete_paper(index: int):
    try:
        del papers[index]
        return {"message": "Paper deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Paper not found")

@app.post("/categories/")
async def create_category(category: Category):
    categories.append(category)
    return {"message": "Category created successfully"}

@app.get("/categories/", response_model=List[Category])
async def get_categories():
    return categories

@app.get("/papers/{paper_id}/categories", response_model=List[Category])
async def get_categories_for_paper(paper_id: int):
    return [category for category in categories if category.paper_id == paper_id]

