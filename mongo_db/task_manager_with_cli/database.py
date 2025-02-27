# Lesson PyMongo and CRUD Operations                            Date 26/02/2025

# Exercise n2 Task Manager with a Command-Line Interface

from pymongo import MongoClient
from pymongo.database import Database


def get_database() -> Database:
    """Establishes a connection to the MongoDB database and returns the database instance."""
    client = MongoClient("mongodb://localhost:27017/")
    return client["task_manager"]