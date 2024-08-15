 # 3. Develop a CLI Based todo application

class TodoApp:
    def _init_(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added!")

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

    def delete_task(self):
        task_number = int(input("Enter the task number to delete: ")) - 1
        if task_number < len(self.tasks):
            del self.tasks[task_number]
            print("Task deleted!")
        else:
            print("Invalid task number!")

    def mark_done(self):
        task_number = int(input("Enter the task number to mark as done: ")) - 1
        if task_number < len(self.tasks):
            self.tasks[task_number]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")

    def run(self):
        while True:
            print("\nTodo App")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Done")
            print("5. Quit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_done()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again!")

if __name_ == "__main_":
    app = TodoApp()
    app.run()
