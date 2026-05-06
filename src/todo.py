# src/todo.py

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, task):
        self.todos.append({"task": task, "done": False})

    def complete(self, index):
        self.todos[index]["done"] = True

    def get_all(self):
        return self.todos

    def delete(self, index):
        self.todos.pop(index)
