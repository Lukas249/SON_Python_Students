import datetime

from GitProject.attendance.attendance import Attendance
from GitProject.students.student import Student

class ParseAttendance:
    @staticmethod
    def txt(lines: list[str]) -> Attendance:
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

        attendance = Attendance(students, date)
        attendance.presence = presence

        return attendance

    @staticmethod
    def csv(lines: list[str]) -> Attendance:
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

        attendance = Attendance(students, date)
        attendance.presence = presence

        return attendance