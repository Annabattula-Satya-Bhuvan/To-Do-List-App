```python
# Console-Based To-Do List Application

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\n------ Your Tasks ------")
            for i, task in enumerate(tasks, start=1):
                status = "✔ Completed" if task["completed"] else "✖ Pending"
                print(f"{i}. {task['task']} - {status}")

    # Mark Task as Completed
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✖"
                print(f"{i}. {task['task']} [{status}]")

            try:
                task_no = int(input("Enter task number: "))
                tasks[task_no - 1]["completed"] = True
                print("✅ Task marked as completed!")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                task_no = int(input("Enter task number: "))
                removed = tasks.pop(task_no - 1)
                print(f"🗑 '{removed['task']}' deleted successfully!")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

    # Exit
    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
```
