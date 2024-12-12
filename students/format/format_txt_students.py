from SON_Python_Students.students.format.base_format_students import BaseFormatStudents
from SON_Python_Students.students.student import Student


class FormatStudentsTXT(BaseFormatStudents):

    @staticmethod
    def format(students: list[Student]) -> list[str]:
        lines = []

        for i in range(len(students)):
            student = students[i].dict(["Name", "Surname", "ID"])

            line = []

            for student_key in student:
                if student_key == "ID":
                    line.append("-")

                line.append(student[student_key])

            line = " ".join(line)

            if i < len(students) - 1:
                line += "\n"

            lines.append(line)

        return lines