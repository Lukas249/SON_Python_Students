class Student:
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id

    def dict(self, keys: list[str]) -> dict[str, str]:
        return {
            keys[0]: self.name,
            keys[1]: self.surname,
            keys[2]: self.id
        }