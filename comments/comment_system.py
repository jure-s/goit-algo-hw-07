import json

class Comment:
    def __init__(self, text, author, replies=None, is_deleted=False):
        """Ініціалізація коментаря"""
        self.text = text
        self.author = author
        self.replies = replies if replies else []
        self.is_deleted = is_deleted

    def add_reply(self, reply):
        """Додає відповідь до коментаря"""
        self.replies.append(reply)

    def remove_reply(self):
        """Позначає коментар як видалений"""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        """Рекурсивно виводить коментарі та відповіді"""
        prefix = "    " * indent
        print(f"{prefix}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(indent + 1)

    def to_dict(self):
        """Перетворює об'єкт коментаря у словник для збереження"""
        return {
            "text": self.text,
            "author": self.author,
            "is_deleted": self.is_deleted,
            "replies": [reply.to_dict() for reply in self.replies]
        }

    @classmethod
    def from_dict(cls, data):
        """Створює об'єкт коментаря з JSON-даних"""
        replies = [cls.from_dict(reply) for reply in data["replies"]]
        return cls(data["text"], data["author"], replies, data["is_deleted"])

def save_comments(comments, filename="comments.json"):
    """Зберігає коментарі у файл"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([comment.to_dict() for comment in comments], f, ensure_ascii=False, indent=4)

def load_comments(filename="comments.json"):
    """Завантажує коментарі з файлу"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Comment.from_dict(comment) for comment in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
