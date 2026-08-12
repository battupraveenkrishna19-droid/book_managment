import streamlit as st
import requests


API_URL = "https://book-managment-3.onrender.com"


st.set_page_config(
    page_title="Book Management System",
    page_icon="📚",
    layout="wide"
)


st.title("📚 Book Management System")
st.write("Manage your books using FastAPI + Streamlit")


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select an option",
    [
        "View Books",
        "Add Book",
        "Update Book",
        "Delete Book"
    ]
)


# -----------------------------
# View Books
# -----------------------------

if menu == "View Books":

    st.header("📖 All Books")

    response = requests.get(f"{API_URL}/books")

    if response.status_code == 200:

        books = response.json()

        if len(books) == 0:

            st.info("No books available.")

        else:

            for book in books:

                with st.container():

                    col1, col2, col3, col4, col5 = st.columns(5)

                    col1.write(f"**ID:** {book['id']}")
                    col2.write(f"**Title:** {book['title']}")
                    col3.write(f"**Author:** {book['author']}")
                    col4.write(f"**Price:** ₹{book['price']}")
                    col5.write(
                        f"**Quantity:** {book['quantity']}"
                    )

                    st.divider()

    else:

        st.error("Unable to connect to FastAPI.")


# -----------------------------
# Add Book
# -----------------------------

elif menu == "Add Book":

    st.header("➕ Add New Book")

    title = st.text_input("Book Title")

    author = st.text_input("Author")

    price = st.number_input(
        "Price",
        min_value=0.0,
        step=1.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )

    if st.button("Add Book"):

        data = {
            "title": title,
            "author": author,
            "price": price,
            "quantity": quantity
        }

        response = requests.post(
            f"{API_URL}/books",
            json=data
        )

        if response.status_code == 200:

            st.success("Book added successfully!")

        else:

            st.error("Failed to add book.")


# -----------------------------
# Update Book
# -----------------------------

elif menu == "Update Book":

    st.header("✏️ Update Book")

    book_id = st.number_input(
        "Book ID",
        min_value=1,
        step=1
    )

    title = st.text_input("New Title")

    author = st.text_input("New Author")

    price = st.number_input(
        "New Price",
        min_value=0.0,
        step=1.0
    )

    quantity = st.number_input(
        "New Quantity",
        min_value=0,
        step=1
    )

    if st.button("Update Book"):

        data = {
            "title": title,
            "author": author,
            "price": price,
            "quantity": quantity
        }

        response = requests.put(
            f"{API_URL}/books/{book_id}",
            json=data
        )

        if response.status_code == 200:

            st.success("Book updated successfully!")

        else:

            st.error("Book not found.")


# -----------------------------
# Delete Book
# -----------------------------

elif menu == "Delete Book":

    st.header("🗑️ Delete Book")

    book_id = st.number_input(
        "Book ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Book"):

        response = requests.delete(
            f"{API_URL}/books/{book_id}"
        )

        if response.status_code == 200:

            st.success("Book deleted successfully!")

        else:

            st.error("Book not found.")
