import datetime
from abc import abstractmethod

from attendance.attendance import Attendance
from students.student import Student

class BaseParseAttendance:
    @staticmethod
    @abstractmethod
    def parse(lines: list[str]) -> Attendance:
        pass

class ParseAttendanceTXT(BaseParseAttendance):

    @staticmethod
    def parse(lines: list[str]) -> Attendance:
        students = []

        date_list = [int(x) for x in lines[0].split(":")[1].split(".")]
        date = datetime.datetime(date_list[2], date_list[1], date_list[0])

        presence = {}

        for i in range(1, len(lines)):
            line = lines[i].rstrip()

            student_details = [j for i in line.split(" - ") for j in i.split(" ")]

            student = Student(
                student_details[0],
                student_details[1],
                student_details[2]
            )

            presence[student.id] = True if student_details[3] == "True" else False

            students.append(student)

        return Attendance(students, date, presence)

class ParseAttendanceCSV(BaseParseAttendance):

    @staticmethod
    def parse(lines: list[str]) -> Attendance:
        students = []

        date_list = [int(x) for x in lines[0].split(":")[1].split(".")]
        date = datetime.datetime(date_list[2], date_list[1], date_list[0])

        presence = {}

        for i in range(1, len(lines)):
            line = lines[i].rstrip()

            student_details = line.split(";")

            student = Student(
                student_details[0],
                student_details[1],
                student_details[2]
            )

            presence[student.id] = True if student_details[3] == "True" else False

            students.append(student)

        return Attendance(students, date, presence)