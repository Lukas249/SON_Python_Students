from SON_Python_Students.students.parse.base_parse_students import BaseParseStudents
from SON_Python_Students.students.student import Student


class ParseStudentsCSV(BaseParseStudents):

    @staticmethod
    def parse(lines: list[str]) -> list[Student]:
        students = []

        for line in lines:
            line = line.rstrip()

            student_details = line.split(";")

            student = Student(
                student_details[0],
                student_details[1],
                student_details[2]
            )

            students.append(student)

        return students