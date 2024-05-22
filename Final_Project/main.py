# main.py
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas
import crud
import dramatiq
from dramatiq_action import borrow_book_async
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

from database import SessionLocal, engine
import models
import schemas
import crud
from utils import create_access_token, verify_token

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": 'obsidian'})

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authorization function
def check_authorization(token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

# User registration
@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

# Token generation (login)
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# CRUD endpoints
@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Author, author)

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Author, skip=skip, limit=limit)

@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Author, author_id)

@app.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Author, author_id, author)

@app.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Author, author_id)

# Repeat similar endpoints for other models: Book, Genre, Library, Loan, Member, Publisher, Review, Section, Staff

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Book, book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Book, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Book, book_id)

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Book, book_id, book)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Book, book_id)

# Add similar endpoints for Genre, Library, Loan, Member, Publisher, Review, Section, Staff

@app.post("/genres/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Genre, genre)

@app.get("/genres/", response_model=List[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Genre, skip=skip, limit=limit)

@app.get("/genres/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Genre, genre_id)

@app.put("/genres/{genre_id}", response_model=schemas.Genre)
def update_genre(genre_id: int, genre: schemas.GenreCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Genre, genre_id, genre)

@app.delete("/genres/{genre_id}")
def delete_genre(genre_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Genre, genre_id)

@app.post("/libraries/", response_model=schemas.Library)
def create_library(library: schemas.LibraryCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Library, library)

@app.get("/libraries/", response_model=List[schemas.Library])
def read_libraries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Library, skip=skip, limit=limit)

@app.get("/libraries/{library_id}", response_model=schemas.Library)
def read_library(library_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Library, library_id)

@app.put("/libraries/{library_id}", response_model=schemas.Library)
def update_library(library_id: int, library: schemas.LibraryCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Library, library_id, library)

@app.delete("/libraries/{library_id}")
def delete_library(library_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Library, library_id)

@app.post("/loans/", response_model=schemas.Loan)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Loan, loan)

@app.get("/loans/", response_model=List[schemas.Loan])
def read_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Loan, skip=skip, limit=limit)

@app.get("/loans/{loan_id}", response_model=schemas.Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Loan, loan_id)

@app.put("/loans/{loan_id}", response_model=schemas.Loan)
def update_loan(loan_id: int, loan: schemas.LoanCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Loan, loan_id, loan)

@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Loan, loan_id)

@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Member, member)

@app.get("/members/", response_model=List[schemas.Member])
def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Member, skip=skip, limit=limit)

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Member, member_id)

@app.put("/members/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, member: schemas.MemberCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Member, member_id, member)

@app.delete("/members/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Member, member_id)

@app.post("/publishers/", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Publisher, publisher)

@app.get("/publishers/", response_model=List[schemas.Publisher])
def read_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Publisher, skip=skip, limit=limit)

@app.get("/publishers/{publisher_id}", response_model=schemas.Publisher)
def read_publisher(publisher_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Publisher, publisher_id)

@app.put("/publishers/{publisher_id}", response_model=schemas.Publisher)
def update_publisher(publisher_id: int, publisher: schemas.PublisherCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Publisher, publisher_id, publisher)

@app.delete("/publishers/{publisher_id}")
def delete_publisher(publisher_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Publisher, publisher_id)

@app.post("/reviews/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Review, review)

@app.get("/reviews/", response_model=List[schemas.Review])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Review, skip=skip, limit=limit)

@app.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Review, review_id)

@app.put("/reviews/{review_id}", response_model=schemas.Review)
def update_review(review_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Review, review_id, review)

@app.delete("/reviews/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Review, review_id)

@app.post("/sections/", response_model=schemas.Section)
def create_section(section: schemas.SectionCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Section, section)

@app.get("/sections/", response_model=List[schemas.Section])
def read_sections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Section, skip=skip, limit=limit)

@app.get("/sections/{section_id}", response_model=schemas.Section)
def read_section(section_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Section, section_id)

@app.put("/sections/{section_id}", response_model=schemas.Section)
def update_section(section_id: int, section: schemas.SectionCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Section, section_id, section)

@app.delete("/sections/{section_id}")
def delete_section(section_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Section, section_id)

@app.post("/staffs/", response_model=schemas.Staff)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_object(db, models.Staff, staff)

@app.get("/staffs/", response_model=List[schemas.Staff])
def read_staffs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_objects(db, models.Staff, skip=skip, limit=limit)

@app.get("/staffs/{staff_id}", response_model=schemas.Staff)
def read_staff(staff_id: int, db: Session = Depends(get_db)):
    return crud.get_object(db, models.Staff, staff_id)

@app.put("/staffs/{staff_id}", response_model=schemas.Staff)
def update_staff(staff_id: int, staff: schemas.StaffCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_object(db, models.Staff, staff_id, staff)

@app.delete("/staffs/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_object(db, models.Staff, staff_id)



# @app.post("/borrow/{book_id}/member/{member_id}")
# def borrow_book_api(book_id: int, member_id: int, db: Session = Depends(get_db)):
#     dramatiq_messages = []
#     dramatiq_messages.append(borrow_book_async.send(str(db), book_id, member_id))
#     return {"message": "Book borrowing request received.", "dramatiq_messages": dramatiq_messages}