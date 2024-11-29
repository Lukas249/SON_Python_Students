from abc import abstractmethod

from attendance.attendance import Attendance


class BaseFormatAttendance:
    @staticmethod
    @abstractmethod
    def format(attendance: Attendance) -> list[str]:
        pass