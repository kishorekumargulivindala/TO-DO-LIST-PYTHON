import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{i+1}. {task['title']} [{status}]")

tasks = load_tasks()

while True:
    print("\n========= TO DO LIST =========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Complete")
    print("5. Edit Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added!")

    elif choice == '2':
        show_tasks(tasks)

    elif choice == '3':
        show_tasks(tasks)
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print("Deleted:", removed["title"])

    elif choice == '4':
        show_tasks(tasks)
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task completed!")

    elif choice == '5':
        show_tasks(tasks)
        num = int(input("Enter task number to edit: "))
        if 1 <= num <= len(tasks):
            new_title = input("Enter new task: ")
            tasks[num - 1]["title"] = new_title
            save_tasks(tasks)
            print("Task updated!")

    elif choice == '6':
        print("Goodbye!")
        break