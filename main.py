import argparse
from rich.console import Console
from rich.table import Table
from storage import load_data, save_data, next_id
from models import User, Task

console = Console()


def add_user(args):
    data = load_data()
    data["users"].append(
        User(next_id(data, "user"), args.name, args.email).to_dict()
    )
    save_data(data)
    console.print("User added")


def add_task(args):
    data = load_data()
    user = next((u for u in data["users"] if u["name"] == args.user), None)

    if not user:
        console.print("User not found")
        return

    data["tasks"].append(
        Task(next_id(data, "task"), args.title, user["id"]).to_dict()
    )
    save_data(data)
    console.print("Task added")


def list_tasks(args):
    data = load_data()
    user = next((u for u in data["users"] if u["name"] == args.user), None)

    if not user:
        console.print("User not found")
        return

    table = Table(title=f"Tasks for {user['name']}")
    table.add_column("ID")
    table.add_column("Title")

    for t in data["tasks"]:
        if t["user_id"] == user["id"]:
            table.add_row(str(t["id"]), t["title"])

    console.print(table)


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers()

    p = sub.add_parser("add-user")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)
    p.set_defaults(func=add_user)

    p = sub.add_parser("add-task")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.set_defaults(func=add_task)

    p = sub.add_parser("list-tasks")
    p.add_argument("--user", required=True)
    p.set_defaults(func=list_tasks)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()