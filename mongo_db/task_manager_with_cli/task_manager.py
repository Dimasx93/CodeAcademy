# Lesson PyMongo and CRUD Operations                            Date 26/02/2025

# Exercise n2 Task Manager with a Command-Line Interface

from typing import Any

from bson import ObjectId

from database import get_database


def add_task(task: dict[str, Any]) -> str:
    """Adds a new task to the tasks collection."""
    db = get_database()
    collection = db["tasks"]
    result = collection.insert_one(task)
    return str(result.inserted_id)


def view_all_tasks() -> list[dict[str, Any]]:
    """Fetches all tasks from the tasks collection."""
    db = get_database()
    collection = db["tasks"]
    return list(collection.find())


def update_task_status(task_id: str, status: str) -> int:
    """Updates the status of a task by its ID."""
    db = get_database()
    collection = db["tasks"]
    result = collection.update_one(
        {"_id": ObjectId(task_id)}, {"$set": {"status": status}}
    )
    return result.modified_count


def delete_task(task_id: str) -> int:
    """Deletes a task by its ID."""
    db = get_database()
    collection = db["tasks"]
    result = collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count