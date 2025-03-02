# Lesson MongoDB Schema validation                                 date 27/02/2025

#Exercise n2 Library Manager with Schema Validation

from typing import Any

from bson import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
from pymongo import errors as pymongo_errors


class LibraryManager:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        try:
            self.client = MongoClient(host, port, serverSelectionTimeoutMS=5000)
            self.db = self.client[db_name]

            # Define the schema validation rules
            validation_rules = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": ["title", "author", "year", "genre"],
                    "properties": {
                        "title": {
                            "bsonType": "string",
                            "description": "'title' must be a string and is required.",
                        },
                        "author": {
                            "bsonType": "string",
                            "description": "'author' must be a string and is required.",
                        },
                        "year": {
                            "bsonType": "int",
                            "minimum": 0,
                            "description": "'year' must be a non-negative integer and is required.",
                        },
                        "genre": {
                            "bsonType": "string",
                            "description": "'genre' must be a string and is required.",
                        },
                    },
                }
            }

            # Apply schema validation when creating or modifying the collection
            existing_collections = self.db.list_collection_names()
            if collection_name in existing_collections:
                # Modify the existing collection to include validation
                self.db.command(
                    "collMod",
                    collection_name,
                    validator={"$jsonSchema": validation_rules["$jsonSchema"]},
                    validationLevel="strict",
                )
                print(
                    f"Schema validation applied to existing collection '{collection_name}'."
                )
            else:
                # Create a new collection with validation
                self.collection = self.db.create_collection(
                    collection_name,
                    validator={"$jsonSchema": validation_rules["$jsonSchema"]},
                    validationLevel="strict",
                )
                print(f"Collection '{collection_name}' created with schema validation.")

            # Get the collection
            self.collection = self.db[collection_name]

            # Test connection
            self.client.admin.command("ping")
            print("Connected to MongoDB successfully.")
        except pymongo_errors.ConnectionFailure as e:
            print(f"Connection failure: {e}")
            raise
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred during initialization: {e}")
            raise

    def add_book(self, book: dict[str, Any]) -> str:
        try:
            result = self.collection.insert_one(book)
            return str(result.inserted_id)
        except pymongo_errors.DuplicateKeyError as e:
            print(f"Duplicate key error: {e}")
            return ""
        except pymongo_errors.WriteError as e:
            print(f"Write error (validation failed): {e.details['errmsg']}")
            return ""
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while adding a book: {e}")
            return ""

    def get_all_books(self) -> list[dict[str, Any]]:
        try:
            return list(self.collection.find())
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while retrieving all books: {e}")
            return []

    def get_book(self, book_id: str) -> dict[str, Any]:
        try:
            result = self.collection.find_one({"_id": ObjectId(book_id)})
            if result:
                return result
            else:
                print("Book not found.")
                return {}
        except (InvalidId, TypeError) as e:
            print(f"Invalid ObjectId: {e}")
            return {}
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while retrieving the book: {e}")
            return {}

    def update_book(self, book_id: str, updates: dict[str, Any]) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(book_id)}, {"$set": updates}
            )
            if result.modified_count > 0:
                print("Book updated successfully.")
                return True
            else:
                print("No changes made to the book.")
                return False
        except (InvalidId, TypeError) as e:
            print(f"Invalid ObjectId: {e}")
            return False
        except pymongo_errors.WriteError as e:
            print(f"Write error (validation failed): {e.details['errmsg']}")
            return False
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while updating the book: {e}")
            return False

    def delete_book(self, book_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count > 0:
                print("Book deleted successfully.")
                return True
            else:
                print("Book not found or already deleted.")
                return False
        except (InvalidId, TypeError) as e:
            print(f"Invalid ObjectId: {e}")
            return False
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while deleting the book: {e}")
            return False