from students.parse.base_parse_students import BaseParseStudents
from students.student import Student


class ParseStudentsTXT(BaseParseStudents):
    @staticmethod
    def parse(lines: list[str]) -> list[Student]:
        students = []

        for line in lines:
            line = line.rstrip()

            student_details = [j for i in line.split(" - ") for j in i.split(" ")]

            student = Student(
                student_details[0],
                student_details[1],
                student_details[2]
            )

            students.append(student)

        return students