import datetime

class Task:
    task_counter = 1

    def __init__(self, title, description, status="TODO"):
        self.id = Task.task_counter
        Task.task_counter += 1

        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[ID: {self.id}] {self.title} | {self.status} | Created: {self.created_at}"


# List to store all tasks
tasks = []


# CREATE
def create_task():
    print("\n--- Create Task ---")
    title = input("Enter Title: ")
    desc = input("Enter Description: ")
    status = input("Enter Status (TODO / IN_PROGRESS / DONE): ").upper()

    if status == "":
        status = "TODO"

    t = Task(title, desc, status)
    tasks.append(t)
    print("Task created successfully!\n")


# READ - LIST
def list_tasks():
    print("\n--- All Tasks ---")
    if len(tasks) == 0:
        print("No tasks found.\n")
        return
    for t in tasks:
        print(t)
    print()


# READ - VIEW ONE
def view_task():
    task_id = int(input("Enter Task ID: "))
    for t in tasks:
        if t.id == task_id:
            print("\n--- Task Details ---")
            print(f"ID: {t.id}")
            print(f"Title: {t.title}")
            print(f"Description: {t.description}")
            print(f"Status: {t.status}")
            print(f"Created At: {t.created_at}\n")
            return
    print("Task not found.\n")


# UPDATE
def update_task():
    task_id = int(input("Enter Task ID to Update: "))
    for t in tasks:
        if t.id == task_id:
            print("\nLeave field blank to keep old value.\n")

            new_title = input("New Title: ")
            new_desc = input("New Description: ")
            new_status = input("New Status (TODO / IN_PROGRESS / DONE): ").upper()

            if new_title != "":
                t.title = new_title
            if new_desc != "":
                t.description = new_desc
            if new_status != "":
                t.status = new_status

            print("Task updated!\n")
            return

    print("Task not found.\n")


# DELETE
def delete_task():
    task_id = int(input("Enter Task ID to Delete: "))
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            print("Task deleted!\n")
            return
    print("Task not found.\n")


# MAIN MENU LOOP
def main():
    while True:
        print("====== TASK MANAGER ======")
        print("1. Create Task")
        print("2. List Tasks")
        print("3. View Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            view_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
