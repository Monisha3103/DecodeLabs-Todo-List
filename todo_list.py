# Initialize data collections
todo_list = []
task_id_counter = 1

while True:
    # Exact menu format from your screenshot
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        if not todo_list:
            print("\nYour To-Do List is currently empty.")
        else:
            print("\nYour Current Tasks:")
            # Displays tasks cleanly using sequential numbering
            for index, item in enumerate(todo_list, 1):
                print(f"{index}. {item['task']}")

    elif choice == "2":
        task_name = input("\nEnter the task you want to add: ").strip()
        if task_name:
            task_row = {
                "id": task_id_counter,
                "task": task_name
            }
            todo_list.append(task_row)
            print(f"'{task_name}' has been added to your list.")
            task_id_counter += 1
        else:
            print("Error: Task description cannot be empty.")

    elif choice == "3":
        if not todo_list:
            print("\nError: No tasks available to remove.")
        else:
            print("")
            # Shows the list first before asking for the number to remove
            for index, item in enumerate(todo_list, 1):
                print(f"{index}. {item['task']}")
            
            try:
                print("")
                target_num = int(input("Enter the number of the task to remove: ").strip())
                # Checks if the chosen number is valid inside our list length
                if 1 <= target_num <= len(todo_list):
                    removed_item = todo_list.pop(target_num - 1)
                    print(f"'{removed_item['task']}' has been removed successfully.")
                else:
                    print(f"Error: Task number {target_num} does not exist.")
            except ValueError:
                print("Error: Please enter a valid number.")

    elif choice == "4":
        print("\nTerminating process... Goodbye!")
        break

    else:
        print("Error: Invalid selection. Please choose an option from 1 to 4.")