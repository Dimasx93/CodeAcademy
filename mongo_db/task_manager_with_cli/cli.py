# Lesson PyMongo and CRUD Operations                            Date 26/02/2025

# Exercise n2 Task Manager with a Command-Line Interface

from typing import Any

from bson.errors import InvalidId

from task_manager import add_task, delete_task, update_task_status, view_all_tasks


def display_tasks(tasks: list[dict[str, Any]]) -> None:
    """Displays tasks in a user-friendly format."""
    if not tasks:
        print("No tasks found.")
        return

    print("TASKS:")
    for task in tasks:
        print(f"ID: {task['_id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task.get('status', 'N/A')}")
        print("------------------------")


def add_task_cli() -> None:
    """Handles adding a new task via CLI."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "status": "Pending"}
    task_id = add_task(task)
    print(f"Task added with ID: {task_id}")


def view_all_tasks_cli() -> None:
    """Handles displaying all tasks via CLI."""
    tasks = view_all_tasks()
    display_tasks(tasks)


def update_task_status_cli() -> None:
    """Handles updating a task's status via CLI."""
    task_id = input("Enter task ID: ")
    try:
        status = input("Enter new status (e.g., Completed, In Progress): ")
        count = update_task_status(task_id, status)
        if count > 0:
            print("Task updated successfully.")
        else:
            print("No task found with the given ID.")
    except InvalidId:
        print("Invalid Task ID format.")


def delete_task_cli() -> None:
    """Handles deleting a task via CLI."""
    task_id = input("Enter task ID: ")
    try:
        count = delete_task(task_id)
        if count > 0:
            print("Task deleted successfully.")
        else:
            print("No task found with the given ID.")
    except InvalidId:
        print("Invalid Task ID format.")


def display_menu() -> None:
    """Displays the main menu for the task manager."""
    print("\nTASK MANAGER MENU")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")


def main() -> None:
    """Main function to handle user interactions."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task_cli()
        elif choice == "2":
            view_all_tasks_cli()
        elif choice == "3":
            update_task_status_cli()
        elif choice == "4":
            delete_task_cli()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()