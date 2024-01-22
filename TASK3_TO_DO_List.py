tasks = []
def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the # to delete: "))
        if 0 <= task_to_delete < len(tasks):
            deleted_task = tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} ('{deleted_task}') has been removed.")
        else:
            print(f"Task #{task_to_delete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    while True:
        print("\n")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        else: 
            print("Done")
            break