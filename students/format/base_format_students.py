from abc import abstractmethod

from SON_Python_Students.students.student import Student


class BaseFormatStudents:

    @staticmethod
    @abstractmethod
    def format(students: list[Student]) -> list[str]:
        pass