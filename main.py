import argparse
from rich.console import Console
from rich.table import Table

from storage import load_data, save_data, next_id
from models import User, Project, Task

console = Console()

def add_user(args):
    data = load_data()
    user_id = next_id(data, "user")

    user = User(user_id, args.name, args.email)
    data["users"].append(user.to_dict())
    save_data(data)

    console.print(f"[green]User added:[/green] {args.name}")


def list_users(args):
    data = load_data()
    table = Table(title="Users")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for u in data["users"]:
        table.add_row(str(u["id"]), u["name"], u["email"])

    console.print(table)

def add_project(args):
    data = load_data()

    user = next((u for u in data["users"] if u["name"] == args.user), None)
    if not user:
        console.print("[red]User not found[/red]")
        return

    project_id = next_id(data, "project")
    project = Project(project_id, args.title, user["id"])

    data["projects"].append(project.to_dict())
    save_data(data)

    console.print(f"[green]Project added:[/green] {args.title}")



def add_task(args):
    data = load_data()

    project = next((p for p in data["projects"] if p["title"] == args.project), None)
    if not project:
        console.print("[red]Project not found[/red]")
        return

    task_id = next_id(data, "task")
    task = Task(task_id, args.title, project["id"])

    data["tasks"].append(task.to_dict())
    save_data(data)

    console.print(f"[green]Task added:[/green] {args.title}")


def list_tasks(args):
    data = load_data()

    project = next((p for p in data["projects"] if p["title"] == args.project), None)
    if not project:
        console.print("[red]Project not found[/red]")
        return

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

    task = next((t for t in data["tasks"] if t["id"] == args.id), None)
    if not task:
        console.print("[red]Task not found[/red]")
        return

    task["status"] = "done"
    save_data(data)

    console.print("[green]Task completed[/green]")

def main():
    parser = argparse.ArgumentParser(description="SimpleTracker CLI")
    subparsers = parser.add_subparsers()

    # add-user
    parser_user = subparsers.add_parser("add-user")
    parser_user.add_argument("--name", required=True)
    parser_user.add_argument("--email", required=True)
    parser_user.set_defaults(func=add_user)

    # list-users
    parser_list = subparsers.add_parser("list-users")
    parser_list.set_defaults(func=list_users)

    # add-project
    parser_project = subparsers.add_parser("add-project")
    parser_project.add_argument("--user", required=True)
    parser_project.add_argument("--title", required=True)
    parser_project.set_defaults(func=add_project)

    # add-task
    parser_task = subparsers.add_parser("add-task")
    parser_task.add_argument("--project", required=True)
    parser_task.add_argument("--title", required=True)
    parser_task.set_defaults(func=add_task)

    # list-tasks
    parser_list_tasks = subparsers.add_parser("list-tasks")
    parser_list_tasks.add_argument("--project", required=True)
    parser_list_tasks.set_defaults(func=list_tasks)

    # complete-task
    parser_complete = subparsers.add_parser("complete-task")
    parser_complete.add_argument("--id", type=int, required=True)
    parser_complete.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()