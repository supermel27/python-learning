from fastapi import FastAPI, HTTPException

from .schemas import Book, BookCreate
from .repository import BookRepository
from .database import init_db


app = FastAPI()
repo = BookRepository()

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/books", response_model=list[Book])
def list_books(author: str | None = None, is_read: bool | None = None):
    return repo.get_all(author=author, is_read=is_read)


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = repo.get_by_id(book_id)
    if book is None:
        raise HTTPException(404, "Book not found")
    return book


@app.post("/books", response_model=Book, status_code=201)
def create_book(data: BookCreate):
    new_id = repo.add(data.title, data.author, data.year)
    return repo.get_by_id(new_id)


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookCreate):
    if repo.get_by_id(book_id) is None:
        raise HTTPException(404, "Book not found")
    repo.update(book_id, data.title, data.author, data.year)
    return repo.get_by_id(book_id)


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if repo.get_by_id(book_id) is None:
        raise HTTPException(404, "Book not found")
    repo.delete(book_id)
    return {"message": "Book deleted"}


@app.patch("/books/{book_id}/read", response_model=Book)
def mark_as_read(book_id: int):
    if repo.get_by_id(book_id) is None:
        raise HTTPException(404, "Book not found")
    repo.mark_as_read(book_id)
    return repo.get_by_id(book_id)

