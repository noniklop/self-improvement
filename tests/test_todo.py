from src.todo import TodoList
import pytest

def test_add_task():
    todo = TodoList()
    todo.add("Buy milk")
    assert len(todo.get_all()) == 1
    assert todo.get_all()[0]["task"] == "Buy milk"
    assert todo.get_all()[0]["done"] == False

def test_add_empty_task():
    todo = TodoList()
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        todo.add("")

def test_complete_task():
    todo = TodoList()
    todo.add("Buy milk")
    todo.complete(0)
    assert todo.get_all()[0]["done"] == True

def test_complete_task_out_of_range():
    todo = TodoList()
    with pytest.raises(IndexError):
        todo.complete(1)

def test_delete_task():
    todo = TodoList()
    todo.add("Buy milk")
    todo.delete(0)
    assert len(todo.get_all()) == 0

def test_delete_task_out_of_range():
    todo = TodoList()
    with pytest.raises(IndexError):
        todo.delete(0)

def test_get_completed_tasks():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Clean room")
    todo.complete(0)
    completed = todo.get_completed()
    assert len(completed) == 1
    assert completed[0]["task"] == "Buy milk"
    assert completed[0]["done"] == True

def test_get_pending_tasks():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Clean room")
    todo.complete(0)
    pending = todo.get_pending()
    assert len(pending) == 1
    assert pending[0]["task"] == "Clean room"
    assert pending[0]["done"] == False

def test_get_task():
    todo = TodoList()
    todo.add("Buy milk")
    task = todo.get_task(0)
    assert task is not None
    assert task["task"] == "Buy milk"
    assert task["done"] == False

def test_get_task_out_of_range():
    todo = TodoList()
    assert todo.get_task(0) is None

def test_clear_completed():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Clean room")
    todo.complete(0)
    todo.clear_completed()
    tasks = todo.get_all()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Clean room"
    assert tasks[0]["done"] == False
