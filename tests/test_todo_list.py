from scripts.deploy_todo_list import deploy_todo_list


def test_create_todo():
    todo_list = deploy_todo_list()
    todo_list.createTodo("Test todo.")
    assert todo_list.todoCount() == 1
    assert todo_list.todos(1) == (1, 'Test todo.', False)


def test_toggle_completed():
    todo_list = deploy_todo_list()
    todo_list.createTodo("Test todo.")
    todo_list.toggleCompleted(1)
    assert todo_list.todos(1) == (1, 'Test todo.', True)
