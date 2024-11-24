from students.student import Student


class FormatStudents:
    @staticmethod
    def format_to_txt(students: list[Student]) -> list[str]:
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

    @staticmethod
    def format_to_csv(students: list[Student]) -> list[str]:
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