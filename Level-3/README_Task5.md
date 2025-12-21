README – Task 5: Persistent CRUD Application (Python):
Cognifyz Technologies – Software Development Internship
 Task Objective:

The objective of Task 5 is to upgrade the existing CRUD Task Manager (Task 3) by enabling persistent storage using File I/O.
This ensures that tasks remain saved even after the program is closed and loaded again when restarted.

Features Implemented:
 1. Persistent Storage (File I/O)

All tasks are saved in a text file named tasks.txt.

Data format used:

ID|TITLE|DESCRIPTION|STATUS|CREATED_AT


Application loads tasks at startup and saves them after every CRUD operation.

 2. File Read & Write Logic

Reads from file at program start

Writes updated task list after Create, Update, and Delete

Handles file errors with try-except

 3. CRUD Operations (Enhanced Version)

All operations from Task 3 are retained:

Operation	Functionality
Create	Add new task and save to file
Read	List all tasks / view specific task
Update	Modify task details and save
Delete	Remove task from list and file
4. Error Handling

File missing → program creates a new one

Corrupted lines → automatically skipped

Invalid input → handled gracefully

 Technologies Used:

a.Python 3.x

b.File I/O (open, read, write)

c.Exception handling

d.OOP concepts

How to Run the Program

a.Open Terminal / Command Prompt

b.Navigate to the project folder:

Run the program:

python Task-5.py

 Testing Persistence (Required for Task 5)

Follow these steps to test and record the output:

1.Create tasks

Example:

Study Python

Prepare Resume

Complete Assignment

2️.Exit the program

Choose:

6. Exit

Run the program again
python Task-5.py

confirm your tasks are still visible

If tasks appear → Persistence is working perfectly.

Sample Output:
====== PERSISTENT TASK MANAGER ======
1. Create Task
2. List Tasks
3. View Task
4. Update Task
5. Delete Task
6. Exit
Enter choice: 2

--- All Tasks ---
[ID: 1] Study Python | TODO | Created: 2025-12-04 12:33:10
[ID: 2] Prepare Resume | IN_PROGRESS | Created: 2025-12-04 12:35:22

Output Demonstration (Video Included)

The file task5_demo.mp4 shows:

✔ Running the program
✔ Creating new tasks
✔ Listing the tasks
✔ Exiting and reopening
✔ Tasks still present (persistence confirmed)
✔ Updating and deleting tasks
✔ Smooth exit

This fulfills Cognifyz's requirement for Task 5.

Conclusion:

Task 5 successfully demonstrates:

1.Persistent task storage.

2.File reading and writing.

3.Proper error handling.

4.Enhanced CRUD functionality.

