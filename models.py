class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name.strip()
        self.email = email.strip()

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


class Task:
    def __init__(self, id, title, user_id, status="open"):
        self.id = id
        self.title = title.strip()
        self.user_id = user_id
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "user_id": self.user_id,
            "status": self.status,
        }