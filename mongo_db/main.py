from library_manager import LibraryManager

# Connection details
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "libraryDB"
collection_name = "books"

# Initialize LibraryManager
library = LibraryManager(mongodb_host, mongodb_port, database_name, collection_name)

# Add a book
new_book = {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "year": 1951,
    "genre": "Fiction",
}
book_id = library.add_book(new_book)
print(f"Added book with ID: {book_id}")

# Retrieve all books
print("All books in the library:")
books = library.get_all_books()
for book in books:
    print(book)

# Retrieve a single book by ID
print("Book retrieved by ID:")
book = library.get_book(book_id)
print(book)

# Update the book
updates = {"year": 1952, "genre": "Classic Fiction"}
updated = library.update_book(book_id, updates)
print(f"Book updated: {updated}")

# Delete the book
deleted = library.delete_book(book_id)
print(f"Book deleted: {deleted}")