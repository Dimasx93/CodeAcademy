# Lesson MongoDB Schema validation                                 date 27/02/2025

#Exercise n2 Library Manager with Schema Validation

from library_schema_validation import LibraryManager

# Connection details
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "libraryDB"
collection_name = "books"

try:
    # Initialize LibraryManager
    library = LibraryManager(mongodb_host, mongodb_port, database_name, collection_name)

    # Add a book with valid data
    new_book = {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "genre": "Fiction",
    }
    book_id = library.add_book(new_book)
    if book_id:
        print(f"Added book with ID: {book_id}")

    # Attempt to add a book that violates the schema (missing 'author')
    print("\nTrying to add a book with missing 'author' field:")
    invalid_book = {
        "title": "1984",
        "year": 1949,
        "genre": "Dystopian",
    }
    library.add_book(invalid_book)

    # Retrieve all books
    print("\nAll books in the library:")
    books = library.get_all_books()
    for book in books:
        print(book)

    # Retrieve a single book by ID
    print("\nRetrieve a single book by ID:")
    if book_id:
        book = library.get_book(book_id)
        print(book)

    # Update a book with valid data
    print("\nUpdating a book with valid data:")
    updates = {"year": 1952, "genre": "Classic Fiction"}
    updated = library.update_book(book_id, updates)
    print(f"Book updated: {updated}")

    # Update a book with invalid data (e.g., 'year' as a string)
    print("\nUpdating a book with invalid data:")
    invalid_updates = {"year": "Nineteen Fifty-Two"}  # Invalid 'year' type
    updated = library.update_book(book_id, invalid_updates)
    print(f"Book updated: {updated}")

    # Delete a book
    print("\nDeleting a book:")
    deleted = library.delete_book(book_id)
    print(f"Book deleted: {deleted}")

except Exception as e:
    print(f"A critical error occurred: {e}")