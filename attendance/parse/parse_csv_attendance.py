import datetime

from SON_Python_Students.attendance.attendance import Attendance
from SON_Python_Students.attendance.parse.base_parse_attendance import BaseParseAttendance
from SON_Python_Students.students.student import Student

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