from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    tags: list[str] = field(default_factory=list)
    creation_date: datetime = field(default_factory=datetime.now)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f'Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nTags: {self.tags}\nCreated on: {self.creation_date}'

class ContactBook:
    pass