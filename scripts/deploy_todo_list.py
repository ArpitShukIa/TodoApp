from brownie import TodoList, network, config
from scripts.helpful_scripts import get_account


def deploy_todo_list():
    account = get_account()
    todo_list = TodoList.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False)
    )
    return todo_list


def main():
    deploy_todo_list()
