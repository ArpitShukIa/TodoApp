from scripts.deploy_todo_list import deploy_todo_list
from scripts.helpful_scripts import get_account


def test_create_todo():
    account = get_account()
    todo_list = deploy_todo_list()
    todo_list.createTodo("Test todo.")
    assert todo_list.todoCount() == 1
    assert todo_list.todos(account, 1) == (1, 'Test todo.', False)


def test_toggle_completed():
    account = get_account()
    todo_list = deploy_todo_list()
    todo_list.createTodo("Test todo.")
    todo_list.toggleCompleted(1)
    assert todo_list.todos(account, 1) == (1, 'Test todo.', True)
