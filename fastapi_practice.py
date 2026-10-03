from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BookBase(BaseModel):
    title: str
    author: str
    year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    is_read: bool = False


books: dict[int, dict] = {}
next_id = 1

# @app.get("/books")
# def get_books():
#     return list(books.values())

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(404, "Book not found") 
    return books[book_id]

@app.post("/books", status_code=201)
def create_book(data: BookCreate):
    global next_id
    new_book = {
        "id": next_id, 
        "title": data.title, 
        "author": data.author, 
        "year": data.year, 
        "is_read": False
    }
    books[next_id] = new_book
    next_id += 1
    return new_book

@app.put("/books/{book_id}")
def update_book(book_id: int, data: BookCreate):
    if book_id not in books:
        raise HTTPException(404, "Book not found") 
    books[book_id]["title"] = data.title
    books[book_id]["author"] = data.author
    books[book_id]["year"] = data.year
    return books[book_id]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(404, "Book not found") 
    del books[book_id]
    return {"message": "Book deleted"}

@app.patch("/books/{book_id}/read")
def mark_read(book_id: int):
    if book_id not in books:
        raise HTTPException(404, "Book not found")
    books[book_id]["is_read"] = True
    return {"message": "Book has been read"}

# @app.get("/books")
# def list_books_by_author(author: str | None = None):
#     result = list(books.values())
#     if author is not None:
#         result = [book for book in result if book["author"] == author]
#     return result

# @app.get("/books")
# def list_books_by_read(is_read: bool | None = None):
#     result = list(books.values())
#     if is_read is not None:
#         result = [book for book in result if book["is_read"] == is_read]
#     return result

@app.get("/books")
def list_books(author: str | None = None, is_read: bool | None = None):
    result = list(books.values())

    if author is not None:
        result = [book for book in result if book["author"] == author]

    if is_read is not None:
        result = [book for book in result if book["is_read"] == is_read]

    return result