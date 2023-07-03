# # To Do List using python3

# A to-do list is a list of tasks or activities that need to be completed within a certain timeframe. 
# It is a helpful tool for organizing and prioritizing tasks to ensure productivity and efficient time management. 
# To-do lists can be used for personal, professional, or academic purposes and To do list provides you with access to add a task set it as complete
# when done allows you to delete the task too within command line interface.

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task}' deleted task successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n**==== To-Do List ====**")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the to-do list. Goodbye! for now Do revisit!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
