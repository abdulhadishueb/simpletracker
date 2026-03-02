import argparse
from rich.console import Console
from rich.table import Table

from storage import load_data, save_data, next_id
from models import User, Task

console = Console()


def find_user(data, name):
    return next((u for u in data["users"] if u["name"] == name), None)


def add_user(args):
    data = load_data()
    user = User(next_id(data, "user"), args.name, args.email)
    data["users"].append(user.to_dict())
    save_data(data)
    console.print(f"[green]User added[/green]: {user.name}")


def add_task(args):
    data = load_data()
    user = find_user(data, args.user)
    if not user:
        console.print("[red]User not found[/red]")
        return

    task = Task(next_id(data, "task"), args.title, user["id"])
    data["tasks"].append(task.to_dict())
    save_data(data)
    console.print(f"[green]Task added[/green]: {task.title}")


def list_tasks(args):
    data = load_data()
    user = find_user(data, args.user)
    if not user:
        console.print("[red]User not found[/red]")
        return

    tasks = [t for t in data["tasks"] if t["user_id"] == user["id"]]

    table = Table(title=f"Tasks for {user['name']}")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")

    for t in tasks:
        table.add_row(str(t["id"]), t["title"], t["status"])

    console.print(table)


def complete_task(args):
    data = load_data()
    task = next((t for t in data["tasks"] if t["id"] == args.id), None)
    if not task:
        console.print("[red]Task not found[/red]")
        return

    task["status"] = "done"
    save_data(data)
    console.print("[green]Task completed[/green]")


def main():
    parser = argparse.ArgumentParser(description="Simple User Task Tracker")
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

    p = sub.add_parser("complete-task")
    p.add_argument("--id", type=int, required=True)
    p.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()