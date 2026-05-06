from typing import List, Dict, Any

class TodoList:
    """
    A class to manage a simple to-do list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty to-do list.
        """
        self.todos: List[Dict[str, Any]] = []

    def add(self, task: str) -> None:
        """
        Add a new task to the to-do list.

        :param task: The task description.
        :raises ValueError: If the task description is empty or only whitespace.
        """
        if not task.strip():
            raise ValueError("Task description cannot be empty.")
        self.todos.append({"task": task.strip(), "done": False})

    def complete(self, index: int) -> None:
        """
        Mark a task as completed by its index.

        :param index: The index of the task to mark as completed.
        :raises IndexError: If the index is out of range.
        """
        if not self._is_valid_index(index):
            raise IndexError("Task index out of range.")
        self.todos[index]["done"] = True

    def get_all(self) -> List[Dict[str, Any]]:
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
        if not self._is_valid_index(index):
            raise IndexError("Task index out of range.")
        self.todos.pop(index)

    def get_completed(self) -> List[Dict[str, Any]]:
        """
        Get a list of all completed tasks.

        :return: A list of completed tasks.
        """
        return [task for task in self.todos if task["done"]]

    def get_pending(self) -> List[Dict[str, Any]]:
        """
        Get a list of all pending tasks.

        :return: A list of pending tasks.
        """
        return [task for task in self.todos if not task["done"]]

    def update(self, index: int, new_task: str) -> None:
        """
        Update the description of an existing task.

        :param index: The index of the task to update.
        :param new_task: The new task description.
        :raises IndexError: If the index is out of range.
        :raises ValueError: If the new task description is empty or only whitespace.
        """
        if not self._is_valid_index(index):
            raise IndexError("Task index out of range.")
        if not new_task.strip():
            raise ValueError("Task description cannot be empty.")
        self.todos[index]["task"] = new_task.strip()

    def clear_completed(self) -> None:
        """
        Remove all completed tasks from the to-do list.
        """
        self.todos = [task for task in self.todos if not task["done"]]

    def _is_valid_index(self, index: int) -> bool:
        """
        Helper method to check if an index is valid.

        :param index: The index to check.
        :return: True if the index is valid, False otherwise.
        """
        return 0 <= index < len(self.todos)
