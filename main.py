import argparse
from rich.console import Console
from rich.table import Table

from storage import load_data, save_data, next_id
from models import User, Project, Task

console = Console()


def add_user(args):
    data = load_data()
    user = User(next_id(data, "user"), args.name, args.email)
    data["users"].append(user.to_dict())
    save_data(data)
    console.print(f"[green]User added[/green]: {user.name}")


def add_project(args):
    data = load_data()
    user = next(u for u in data["users"] if u["name"] == args.user)
    project = Project(next_id(data, "project"), args.title, user["id"])
    data["projects"].append(project.to_dict())
    save_data(data)
    console.print(f"[green]Project added[/green]: {project.title}")


def add_task(args):
    data = load_data()
    project = next(p for p in data["projects"] if p["title"] == args.project)
    task = Task(next_id(data, "task"), args.title, project["id"])
    data["tasks"].append(task.to_dict())
    save_data(data)
    console.print(f"[green]Task added[/green]: {task.title}")


def list_users(args):
    data = load_data()
    table = Table(title="Users")
    table.add_column("ID")
    table.add_column("Name")
    for u in data["users"]:
        table.add_row(str(u["id"]), u["name"])
    console.print(table)


def list_tasks(args):
    data = load_data()
    project = next(p for p in data["projects"] if p["title"] == args.project)
    tasks = [t for t in data["tasks"] if t["project_id"] == project["id"]]

    table = Table(title="Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")

    for t in tasks:
        table.add_row(str(t["id"]), t["title"], t["status"])
    console.print(table)


def complete_task(args):
    data = load_data()
    task = next(t for t in data["tasks"] if t["id"] == args.id)
    task["status"] = "done"
    save_data(data)
    console.print("[green]Task completed[/green]")


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers()

    p = sub.add_parser("add-user")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)
    p.set_defaults(func=add_user)

    p = sub.add_parser("add-project")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.set_defaults(func=add_project)

    p = sub.add_parser("add-task")
    p.add_argument("--project", required=True)
    p.add_argument("--title", required=True)
    p.set_defaults(func=add_task)

    p = sub.add_parser("list-users")
    p.set_defaults(func=list_users)

    p = sub.add_parser("list-tasks")
    p.add_argument("--project", required=True)
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