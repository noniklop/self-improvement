from typing import List, Dict, Any, Optional

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
        :raises ValueError: If the task is already completed.
        """
        if not self._is_valid_index(index):
            raise IndexError(f"Task index {index} is out of range.")
        if self.todos[index]["done"]:
            raise ValueError(f"Task at index {index} is already completed.")
        self.todos[index]["done"] = True

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get the list of all tasks.

        :return: A list of tasks with their completion status.
        """
        return self.todos.copy()

    def delete(self, index: int) -> None:
        """
        Delete a task by its index.

        :param index: The index of the task to delete.
        :raises IndexError: If the index is out of range.
        """
        if not self._is_valid_index(index):
            raise IndexError(f"Task index {index} is out of range.")
        self.todos.pop(index)

    def get_completed(self) -> List[Dict[str, Any]]:
        """
        Get a list of all completed tasks.

        :return: A list of completed tasks.
        """
        return [task.copy() for task in self.todos if task["done"]]

    def get_pending(self) -> List[Dict[str, Any]]:
        """
        Get a list of all pending tasks.

        :return: A list of pending tasks.
        """
        return [task.copy() for task in self.todos if not task["done"]]

    def update(self, index: int, new_task: str) -> None:
        """
        Update the description of an existing task.

        :param index: The index of the task to update.
        :param new_task: The new task description.
        :raises IndexError: If the index is out of range.
        :raises ValueError: If the new task description is empty or only whitespace.
        """
        if not self._is_valid_index(index):
            raise IndexError(f"Task index {index} is out of range.")
        if not new_task.strip():
            raise ValueError("Task description cannot be empty.")
        self.todos[index]["task"] = new_task.strip()

    def clear_completed(self) -> None:
        """
        Remove all completed tasks from the to-do list.
        """
        self.todos = [task for task in self.todos if not task["done"]]

    def count_tasks(self) -> Dict[str, int]:
        """
        Count the total, completed, and pending tasks.

        :return: A dictionary with the counts of total, completed, and pending tasks.
        """
        total = len(self.todos)
        completed = len(self.get_completed())
        pending = len(self.get_pending())
        return {"total": total, "completed": completed, "pending": pending}

    def get_task(self, index: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a task by its index.

        :param index: The index of the task to retrieve.
        :return: The task as a dictionary, or None if the index is out of range.
        """
        if not self._is_valid_index(index):
            return None
        return self.todos[index].copy()

    def _is_valid_index(self, index: int) -> bool:
        """
        Helper method to check if an index is valid.

        :param index: The index to check.
        :return: True if the index is valid, False otherwise.
        """
        return 0 <= index < len(self.todos)

    def find_task(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Find tasks containing a specific keyword.

        :param keyword: The keyword to search for in tasks.
        :return: A list of tasks that contain the keyword.
        :raises ValueError: If the keyword is empty or only whitespace.
        """
        if not keyword.strip():
            raise ValueError("Keyword cannot be empty.")
        return [task.copy() for task in self.todos if keyword.strip().lower() in task["task"].lower()]

    def bulk_complete(self, indices: List[int]) -> None:
        """
        Mark multiple tasks as completed by their indices.

        :param indices: A list of indices of tasks to mark as completed.
        :raises IndexError: If any index is out of range.
        :raises ValueError: If any task is already completed.
        """
        for index in indices:
            self.complete(index)

    def bulk_delete(self, indices: List[int]) -> None:
        """
        Delete multiple tasks by their indices.

        :param indices: A list of indices of tasks to delete.
        :raises IndexError: If any index is invalid.
        """
        for index in sorted(indices, reverse=True):
            self.delete(index)

    def is_all_completed(self) -> bool:
        """
        Check if all tasks in the to-do list are completed.

        :return: True if all tasks are completed, False otherwise.
        """
        return all(task["done"] for task in self.todos)
