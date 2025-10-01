class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter Task: ").strip().lower()
        if task in self.tasks:
            print("Task already exists.")
        else:
            self.tasks.append(task)
            print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(self.tasks):
                removed = self.tasks.pop(index - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\nChoose an option:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Quit")

            choice = input("Enter choice (1-4): ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
manager = TaskManager()
manager.run()
