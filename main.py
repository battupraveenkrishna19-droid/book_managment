from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = []


class Book(BaseModel):
    title: str
    author: str
    price: float
    quantity: int


# Home
@app.get("/")
def home():
    return {"message": "Welcome to Book Management System"}


# Add Book
@app.post("/books")
def add_book(book: Book):

    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "price": book.price,
        "quantity": book.quantity,
        "status": "Available"
    }

    books.append(new_book)

    return new_book


# Get All Books
@app.get("/books")
def get_books():

    return books


# Get One Book
@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# Update Book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for book in books:

        if book["id"] == book_id:

            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["price"] = updated_book.price
            book["quantity"] = updated_book.quantity

            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )