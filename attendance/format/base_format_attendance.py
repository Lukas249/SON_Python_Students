from abc import abstractmethod

from SON_Python_Students.attendance.attendance import Attendance

class BaseFormatAttendance:
    @staticmethod
    @abstractmethod
    def format(attendance: Attendance) -> list[str]:
        pass