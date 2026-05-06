from src.todo import TodoList

def test_add_task():
    todo = TodoList()
    todo.add("Buy milk")
    assert len(todo.get_all()) == 1
    assert todo.get_all()[0]["task"] == "Buy milk"
    assert todo.get_all()[0]["done"] == False

def test_complete_task():
    todo = TodoList()
    todo.add("Buy milk")
    todo.complete(0)
    assert todo.get_all()[0]["done"] == True

def test_delete_task():
    todo = TodoList()
    todo.add("Buy milk")
    todo.delete(0)
    assert len(todo.get_all()) == 0
