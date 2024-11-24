from students.student import Student


class ParseStudents:
    @staticmethod
    def csv_to_list(lines: list[str]) -> list[Student]:
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

    @staticmethod
    def txt_to_list(lines: list[str]) -> list[Student]:
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