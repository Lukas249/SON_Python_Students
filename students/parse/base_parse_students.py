from abc import abstractmethod

from SON_Python_Students.students.student import Student


class BaseParseStudents:

    @staticmethod
    @abstractmethod
    def parse(lines: list[str]) -> list[Student]:
        pass