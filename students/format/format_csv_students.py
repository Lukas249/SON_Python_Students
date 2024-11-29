from students.format.base_format_students import BaseFormatStudents
from students.student import Student

class FormatStudentsCSV(BaseFormatStudents):

    @staticmethod
    def format(students: list[Student]) -> list[str]:
        lines = []

        for i in range(len(students)):
            student = students[i].dict(["Name", "Surname", "ID"])
            line = []

            for student_key in student:
                line.append(student[student_key])

            line = ";".join(line)

            if i < len(students) - 1:
                line += "\n"

            lines.append(line)

        return lines