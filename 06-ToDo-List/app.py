tasks = []

print("========== TO-DO LIST ==========")

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"✅ '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")