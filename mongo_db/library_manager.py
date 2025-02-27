# Lesson PyMongo and CRUD Operations                            Date 26/02/2025

# Exercise n1 Library Manager
from typing import Any

from bson import ObjectId
from pymongo import MongoClient


class LibraryManager:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_book(self, book: dict[str, Any]) -> str:
        result = self.collection.insert_one(book)
        return str(result.inserted_id)

    def get_all_books(self) -> list[dict[str, Any]]:
        return list(self.collection.find())

    def get_book(self, book_id: str) -> dict[str, Any]:
        try:
            return self.collection.find_one({"_id": ObjectId(book_id)})
        except Exception as e:
            print(f"Error retrieving book: {e}")
            return {}

    def update_book(self, book_id: str, updates: dict[str, Any]) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(book_id)}, {"$set": updates}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating book: {e}")
            return False

    def delete_book(self, book_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting book: {e}")
            return False
