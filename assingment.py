import json
import os


class Task:
    """Class representing a single task."""
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"[{self.id}] {self.title} - {status}"


def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        try:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
        except json.JSONDecodeError:
            return []


def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    with open(filename, "w") as file:
        tasks_data = [task.__dict__ for task in tasks]
        json.dump(tasks_data, file, indent=4)


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title:
        task_id = len(tasks) + 1
        new_task = Task(task_id, title)
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!")
    else:
        print("Task title cannot be empty.")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTask List:")
        for task in tasks:
            print(task)
    print()


def delete_task(tasks):
    """Delete a task by ID."""
    try:
        task_id = int(input("Enter task ID to delete: "))
        task_to_delete = next((task for task in tasks if task.id == task_id), None)
        if task_to_delete:
            tasks.remove(task_to_delete)
            save_tasks(tasks)
            print(f"Task '{task_to_delete.title}' deleted successfully!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")


def complete_task(tasks):
    """Mark a task as completed."""
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        task_to_complete = next((task for task in tasks if task.id == task_id), None)
        if task_to_complete:
            task_to_complete.completed = True
            save_tasks(tasks)
            print(f"Task '{task_to_complete.title}' marked as completed!")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")


def display_menu():
    """Display the command-line menu."""
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")


def menu():
    """Main menu loop."""
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid number (1-5).")


if __name__ == "__main__":
    menu()
