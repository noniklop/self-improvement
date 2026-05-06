from typing import List, Dict

class TodoList:
    """
    A class to manage a simple to-do list.
    """

    def __init__(self):
        """
        Initialize an empty to-do list.
        """
        self.todos: List[Dict[str, object]] = []

    def add(self, task: str) -> None:
        """
        Add a new task to the to-do list.

        :param task: The task description.
        """
        if not task.strip():
            raise ValueError("Task description cannot be empty.")
        self.todos.append({"task": task, "done": False})

    def complete(self, index: int) -> None:
        """
        Mark a task as completed by its index.

        :param index: The index of the task to mark as completed.
        :raises IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.todos):
            raise IndexError("Task index out of range.")
        self.todos[index]["done"] = True

    def get_all(self) -> List[Dict[str, object]]:
        """
        Get the list of all tasks.

        :return: A list of tasks with their completion status.
        """
        return self.todos

    def delete(self, index: int) -> None:
        """
        Delete a task by its index.

        :param index: The index of the task to delete.
        :raises IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.todos):
            raise IndexError("Task index out of range.")
        self.todos.pop(index)

    def get_completed(self) -> List[Dict[str, object]]:
        """
        Get a list of all completed tasks.

        :return: A list of completed tasks.
        """
        return [task for task in self.todos if task["done"]]

    def get_pending(self) -> List[Dict[str, object]]:
        """
        Get a list of all pending tasks.

        :return: A list of pending tasks.
        """
        return [task for task in self.todos if not task["done"]]