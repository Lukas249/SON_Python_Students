from abc import abstractmethod

from SON_Python_Students.attendance.attendance import Attendance


class BaseParseAttendance:
    @staticmethod
    @abstractmethod
    def parse(lines: list[str]) -> Attendance:
        pass