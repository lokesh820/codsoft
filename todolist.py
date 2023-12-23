
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def list_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {'[Completed]' if task['completed'] else '[Pending]'} {task['task']}")

def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print("Task marked as complete")
    else:
        print("Invalid task index")

while True:
    print("Options:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark as complete")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index = int(input("Enter the task number: "))
        mark_completed(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
