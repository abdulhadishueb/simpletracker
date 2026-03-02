class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name.strip()
        self.email = email.strip()

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class Project:
    def __init__(self, id, title, owner_id):
        self.id = id
        self.title = title.strip()
        self.owner_id = owner_id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "owner_id": self.owner_id
        }


class Task:
    def __init__(self, id, title, project_id, status="open"):
        self.id = id
        self.title = title.strip()
        self.project_id = project_id
        self.status = status

    def mark_complete(self):
        self.status = "done"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "project_id": self.project_id,
            "status": self.status
        }