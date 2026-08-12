todo_list = []
task_id_counter = 1

print("====================================")
print("      DECODELABS TO-DO SYSTEM       ")
print("====================================")

while True:
    # User Interface menu with advanced options
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit Engine")
    
    choice = input("\nSelect an option (1-5): ").strip()

    if choice == "1":
        task_name = input("Enter task description: ").strip()
        if task_name:
            # Use a dictionary to define a single task row with a status field
            task_row = {
                "id": task_id_counter,
                "task": task_name,
                "status": "Pending"
            }
            # append(row) -> INSERT INTO your list table
            todo_list.append(task_row)
            print(f"Task '{task_name}' added successfully with ID: {task_id_counter}")
            task_id_counter += 1
        else:
            print("Error: Task description cannot be empty.")

    elif choice == "2":
        if not todo_list:
            print("\nYour To-Do List is currently empty.")
        else:
            print("\n--- CURRENT STATE DATABASE ---")
            print(f"{'ID':<6} | {'STATUS':<10} | {'TASK DESCRIPTION'}")
            print("-" * 50)
            # Iteration loop to print data rows
            for item in todo_list:
                print(f"{item['id']:<6} | {item['status']:<10} | {item['task']}")
            print("-" * 50)

    elif choice == "3":
        if not todo_list:
            print("Error: No tasks available to mark as completed.")
        else:
            try:
                target_id = int(input("Enter the ID of the task to complete: ").strip())
                found = False
                for item in todo_list:
                    if item["id"] == target_id:
                        item["status"] = "Completed"
                        print(f"Task {target_id} has been marked as Completed.")
                        found = True
                        break
                if not found:
                    print(f"Error: Task with ID {target_id} not found.")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

    elif choice == "4":
        if not todo_list:
            print("Error: No tasks available to delete.")
        else:
            try:
                target_id = int(input("Enter the ID of the task to delete: ").strip())
                found = False
                for item in todo_list:
                    if item["id"] == target_id:
                        todo_list.remove(item)
                        print(f"Task {target_id} has been deleted successfully.")
                        found = True
                        break
                if not found:
                    print(f"Error: Task with ID {target_id} not found.")
            except ValueError:
                print("Error: Please enter a valid numerical ID.")

    elif choice == "5":
        print("\nTerminating process... Goodbye!")
        break

    else:
        print("Error: Invalid selection. Please choose an option from 1 to 5.")