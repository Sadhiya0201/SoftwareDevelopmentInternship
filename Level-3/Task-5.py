import datetime
import os

FILE_NAME = "tasks.txt"


class Task:
    def __init__(self, id, title, description, status, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at

    def __str__(self):
        return f"[ID: {self.id}] {self.title} | {self.status} | Created: {self.created_at}"

    def to_line(self):
        return f"{self.id}|{self.title}|{self.description}|{self.status}|{self.created_at}\n"


# ---------------- FILE OPERATIONS ---------------- #

def load_tasks():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks  # No file yet

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    id = int(parts[0])
                    title = parts[1]
                    desc = parts[2]
                    status = parts[3]
                    created_at = parts[4]
                    tasks.append(Task(id, title, desc, status, created_at))
    except Exception as e:
        print("Error reading file:", e)

    return tasks


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for t in tasks:
                file.write(t.to_line())
    except Exception as e:
        print("Error writing to file:", e)


# ---------------- CRUD OPERATIONS ---------------- #

def create_task(tasks):
    print("\n--- Create Task ---")
    title = input("Enter Title: ")
    desc = input("Enter Description: ")
    status = input("Enter Status (TODO/IN_PROGRESS/DONE): ").upper()
    if status == "":
        status = "TODO"

    new_id = 1 if not tasks else max(t.id for t in tasks) + 1
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = Task(new_id, title, desc, status, created_at)
    tasks.append(task)

    save_tasks(tasks)
    print("Task created successfully!\n")


def list_tasks(tasks):
    print("\n--- All Tasks ---")
    if not tasks:
        print("No tasks found.\n")
        return

    for t in tasks:
        print(t)
    print()


def view_task(tasks):
    task_id = int(input("Enter Task ID: "))
    for t in tasks:
        if t.id == task_id:
            print("\n--- Task Details ---")
            print(f"ID: {t.id}")
            print(f"Title: {t.title}")
            print(f"Description: {t.description}")
            print(f"Status: {t.status}")
            print(f"Created: {t.created_at}\n")
            return

    print("Task not found.\n")


def update_task(tasks):
    task_id = int(input("Enter Task ID to Update: "))
    for t in tasks:
        if t.id == task_id:
            print("\nLeave field blank to keep current value.\n")

            new_title = input("New Title: ")
            new_desc = input("New Description: ")
            new_status = input("New Status (TODO/IN_PROGRESS/DONE): ").upper()

            if new_title != "":
                t.title = new_title
            if new_desc != "":
                t.description = new_desc
            if new_status != "":
                t.status = new_status

            save_tasks(tasks)
            print("Task updated!\n")
            return

    print("Task not found.\n")


def delete_task(tasks):
    task_id = int(input("Enter Task ID to Delete: "))
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print("Task deleted!\n")
            return

    print("Task not found.\n")


# ---------------- MAIN MENU ---------------- #

def main():
    tasks = load_tasks()

    while True:
        print("====== PERSISTENT TASK MANAGER ======")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. View Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            view_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
