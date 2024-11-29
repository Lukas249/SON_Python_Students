from abc import abstractmethod

from attendance.attendance import Attendance


class BaseParseAttendance:
    @staticmethod
    @abstractmethod
    def parse(lines: list[str]) -> Attendance:
        pass