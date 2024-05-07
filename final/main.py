from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from pydantic import BaseModel
from database import session,engine

from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from database import session,engine
import uvicorn
from fastapi import FastAPI, Body, Depends
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from app.schemas import UserSchema,UserLoginSchema,CreateAuthor,Author,CreateBook,CreateGenre,Genre,Book,CreateQuote,Quote,BookReview,CreateBookReview
from fastapi import Body
import app.models as db
import bcrypt
from sqlalchemy.exc import SQLAlchemyError
db.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        session.close()


"""
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
"""
@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema) -> str:
    try:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        new_user = db.User(
            fullname=user.fullname,
            email=user.email,
            password=hashed_password.decode('utf-8'),
        )
        session.add(new_user)
        session.commit()
        session.close()
        return signJWT(user.email)
    except SQLAlchemyError as e:
        db.rollback()  # Roll back the transaction in case of an error
        raise HTTPException(status_code=500, detail="Database error occurred")


def check_user(data: UserLoginSchema, session: Session):
    user = session.query(db.User).filter(db.User.email == data.email).first()
    if not user or not bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')):
        return False
    return True

@app.post("/user/login", tags=["user"])
def user_login(user_login_data: UserLoginSchema, session: Session = Depends(get_db)):
    result = check_user(user_login_data, session)
    if result:
        return signJWT(user_login_data.email)
    else:
        return {"message": "Invalid email or password"}

# Only authorized users can add books,authors, genres, quotes, and book reviews
@app.post("/authors", dependencies=[Depends(JWTBearer())], tags=["authors"])
def add_authors(author: CreateAuthor, session: Session = Depends(get_db)) -> str:
    session.add(db.Author(**author.model_dump()))
    session.commit()
    session.close()
    return "Author added successfully"

@app.post("/books", dependencies=[Depends(JWTBearer())], tags=["books"])
def add_books(book: CreateBook, session: Session = Depends(get_db)) -> str:
    session.add(db.Book(**book.model_dump()))
    session.commit()
    session.close()
    return "Book added successfully"

@app.post("/genres", dependencies=[Depends(JWTBearer())], tags=["genres"])
def add_genres(genre:CreateGenre,session: Session = Depends(get_db)) -> str:
    session.add(db.Genre(**genre.model_dump()))
    session.commit()
    session.close()
    return "Genre added successfully"

#Even non-authorized users can see lists of all
#available books,authors,quotes,bookreviews and genres, and users

@app.get("/genres", tags=["genres"])
def get_genres():
    db_genres = session.execute(select(db.Genre)).scalars().all()
    genres= []
    for db_genre in db_genres:
        genres.append(Genre.model_validate(db_genre))
    return genres


@app.get("/books", tags=["books"])
def get_books():
    db_books = session.execute(select(db.Book)).scalars().all()
    books = []
    for db_book in db_books:
        books.append(Book.model_validate(db_book))
    return books

@app.get("/authors", tags=["authors"])
def get_authors():
    db_authors = session.execute(select(db.Author)).scalars().all()
    authors = []
    for db_author in db_authors:
        authors.append(Author.model_validate(db_author))
    return authors
@app.post("/quotes", dependencies=[Depends(JWTBearer())], tags=["quotes"])
def add_quotes(quote: CreateQuote,session: Session = Depends(get_db)) -> str:
    session.add(db.Quote(**quote.model_dump()))
    session.commit()
    session.close()
    return "Quote added successfully"

@app.post("/bookreviews", dependencies=[Depends(JWTBearer())], tags=["bookreviews"])
def add_bookreviews(bookreview:CreateBookReview,session: Session = Depends(get_db)) -> str:
    session.add(db.BookReview(**bookreview.model_dump()))
    session.commit()
    session.close()
    return "BookReview"


#Even non-authorized users can see lists of all
#available books,authors,quotes,bookreviews and genres, and users

@app.get("/genres", tags=["genres"])
def get_genres(session: Session = Depends(get_db)):
    db_genres= session.execute(select(db.Genre)).scalars().all()
    genres = []
    for db_genre in db_genres:
        genres.append(Genre.model_validate(db_genre))
    return genres

@app.get("/books", tags=["books"])
def get_books():
    db_books = session.execute(select(db.Book)).scalars().all()
    books = []
    for db_book in db_books:
        books.append(Book.model_validate(db_book))
    return books

@app.get("/authors", tags=["authors"])
def get_authors():
    db_authors = session.execute(select(db.Author)).scalars().all()
    authors = []
    for db_author in db_authors:
        authors.append(Author.model_validate(db_author))
    return authors



@app.get("/quotes", tags=["quotes"])
def get_quotes(session: Session = Depends(get_db)):
    db_quotes = session.execute(select(db.Quote)).scalars().all()
    quotes= []
    for db_quote in db_quotes:
        quotes.append(Quote.model_validate(db_quote))
    return quotes

@app.get("/bookreviews", tags=["bookreviews"])
def get_bookreviews(session: Session = Depends(get_db)):
    db_bookreviews= session.execute(select(db.BookReview)).scalars().all()
    bookreviews = []
    for db_bookreview in db_bookreviews:
        bookreviews.append(BookReview.model_validate(db_bookreview))
    return bookreviews