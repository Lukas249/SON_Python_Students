from abc import abstractmethod

from students.student import Student


class BaseParseStudents:

    @staticmethod
    @abstractmethod
    def parse(lines: list[str]) -> list[Student]:
        pass