from abc import abstractmethod

from students.student import Student


class BaseFormatStudents:

    @staticmethod
    @abstractmethod
    def format(students: list[Student]) -> list[str]:
        pass