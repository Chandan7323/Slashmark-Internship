# Define an empty list with a descriptive name

#To-Do List App

This Python application provides a user-friendly way to manage your tasks. It allows you to create, view, mark tasks as completed, and remove them from your to-do list.

**Features:**
1.Clear and concise to-do list display: View tasks with their status ("Done" or "Not Done").
2.Easy task addition: Add new tasks with informative messages.
3.Reliable task completion: Mark tasks as completed with clear feedback.
4.Safe task removal: Remove tasks with confirmation and informative messages.
5.Error handling: The application gracefully handles invalid input, providing appropriate messages to guide the user.

Usage:
The application presents a menu with the following options:
1.Display to-do list: View all tasks in your list.
2.Add a task: Enter the task description to add it to your list.
3.Mark a task as completed: Choose a task by its number (displayed when viewing the list) to mark it as completed.
4.Remove a task: Select a task by its number to remove it from the list.
5.Quit: Exit the application.

  

todo_list = []

# Function to display the to-do list with better formatting
def display_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, (task, completed) in enumerate(todo_list, start=1):
            status = "Done" if completed else "Not Done"
            print(f"{i}. {task}: {status}")  # Use colon for better readability

# Function to add a task with improved user feedback
def add_task(task_name):
    task = (task_name, False)
    todo_list.append(task)
    print(f"Added '{task_name}' to your to-do list.")  # Use single quotes for consistency

# Function with error handling for invalid input
def mark_completed(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1] = (todo_list[task_number - 1][0], True)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Similar modification for remove_task function
def remove_task(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Removed task '{removed_task[0]}' from your to-do list.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop with consistent formatting
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number)
    elif choice == '4':
        display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
