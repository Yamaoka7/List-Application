class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

# Example usage:
todo_list = TodoList()
todo_list.add_task("Finish coding project")
todo_list.add_task("Go grocery shopping")
todo_list.add_task("Read a book")
todo_list.show_tasks()
