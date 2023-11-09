class Task:
    def __init__(self, name):
        self.name = name
class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("List of Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. Name: {task.name}")

    def update_task(self, old_name, new_name):
        for task in self.tasks:
            if task.name == old_name:
                task.name = new_name
                print(f"Task '{old_name}' updated successfully.")
                return
        print(f"Task '{old_name}' not found in the TodoList.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task.name}' deleted successfully.")
        else:
            print("Invalid task index. Task not deleted.")
    def clear_tasks(self):
        self.tasks = []
        self.completed_tasks = []
        print("All tasks and completed tasks cleared.")

def main():
    todo_list = TodoList()
    menu_options = {
        '1': todo_list.add_task,
        '2': todo_list.view_tasks,
        '3': todo_list.delete_task,
        '4': todo_list.update_task,
        '5': todo_list.clear_tasks,
        '6': exit
    }

    while True:
        print("\n******** To-Do-List Application ********")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice in menu_options:
            if choice in ('2'):
                menu_options[choice]()
            elif choice in ('3'):
                try:
                    task_index = int(input("Enter the task index: "))
                    menu_options[choice](task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task index.")
            elif choice == '4':
                old_task = input("Enter the task to update: ")
                new_task = input("Enter the new task name: ")
                todo_list.update_task(old_task, new_task)
            elif choice == '5':
                confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
                if confirmation.lower() == 'y':
                    menu_options[choice]()
            elif choice == '6':
                print("Thanks for using this Application!")
                break
            else:
                name = input("Enter the task name: ")
                todo_list.add_task(name)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
