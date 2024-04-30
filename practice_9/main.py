from typing import Annotated, Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Paper(BaseModel):
    id: int
    name: str
    author: str


# DATA BASE example:
papers_db = {
    1: Paper(id=1, name="Introduction to Machine Learning", author="John Doe"),
    2: Paper(id=2, name="Deep Learning in Practice", author="Jane Smith"),
    3: Paper(id=3, name="Natural Language Processing Essentials", author="David Johnson")
}


class DataBaseInteracting:
    def __init__(self, is_authorized=False):
        self.is_authorized = is_authorized

    def premission_check(self):
        if not self.is_authorized:
            raise HTTPException('Not enough permissions')

    def isin_db(self, paper: Paper):
        if paper.id not in papers_db:
            raise HTTPException('Paper do not exist')

    def __call__(self, is_authorized: bool = True):
        self.is_authorized = is_authorized
        return self

check_to_allow = DataBaseInteracting()


@app.post("/paper")
def create_paper(paper: Paper, db_checker = Depends(check_to_allow)):
    db_checker.premission_check()
    if papers.id in papers_db:
        return HTTPException('Paper already exist')
    papers_db[paper.id] = paper
    return papers_db[paper.id]

@app.put("/paper")
def update_paper(paper: Paper, db_checker = Depends(check_to_allow)):
    db_checker.premission_check()
    db_checker.isin_db(paper)
    papers_db[paper.id] = paper
    return papers_db[paper.id]

@app.delete("/paper")
def delete_paper(paper: Paper, db_checker = Depends(check_to_allow)):
    db_checker.premission_check()
    db_checker.isin_db(paper)
    papers_db.pop(paper.id)
    return 'Deleted'




