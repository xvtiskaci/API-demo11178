import json
from dataclasses import dataclass


@dataclass
class User:
    legal_form: str
    name: str
    id_number: int
    chief: str
    contact_person: str
    phone_number: str
    email: str
    address: str
    password: str
    repeat_password: str

    def to_json(self):
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)
