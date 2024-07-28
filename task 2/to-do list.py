print("<<<<<<<<<<<--Welcome To Simple To-Do List App-->>>>>>>>>>>")

# Function to display the menu
def display_menu():
    print("Welcome to To-Do List App")
    print("1. Add task")
    print("2. Edit task")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Mark task as done")
    print("6. Exit")

# Function to add a task
def add_task(tasks, task):
    tasks.append(task)
    print("Task successfully added...")

# Function to edit a task
def edit_task(tasks, index, new_task):
    if index < len(tasks):
        tasks[index] = new_task
        print("Task successfully edited...")
    else:
        print("Invalid task index")

# Function to Delete a task
def delete_task(tasks, index):
    if index < len(tasks):
        del tasks[index]
        print("Task successfully deleted...")
    else:
        print("Invalid task index")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display...")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to mark a task as done
def mark_task_done(tasks, index):
    if index >= 0 and index < len(tasks):
        print(f"Marked task '{tasks[index]}' as done")
        del tasks[index]
    else:
        print("Invalid task index")

# Main function to run the app
def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            index = int(input("Enter task number to edit: ")) - 1
            new_task = input("Enter new task: ")
            edit_task(tasks, index, new_task)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_task_done(tasks, index)
        elif choice == '6':
            print("Thank you for using To-Do List App...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
