from attendance.attendance import Attendance

class FormatAttendance:
    @staticmethod
    def format_to_txt(attendance: Attendance):
        date = attendance.date.strftime("%d.%m.%Y")

        if len(attendance.students) == 0:
            return [f"Date: {date}"]

        lines = [f"Date: {date}\n"]

        student_structure = ["Name", "Surname", "ID"]

        for i in range(len(attendance.presence)):
            student = attendance.students[i].dict(student_structure)

            line = []

            for student_key in student:
                if student_key == "ID":
                    line.append("-")

                line.append(student[student_key])

            student_id = student["ID"]
            student_presence = "True" if attendance.presence[student_id] else "False"

            line.append(student_presence)

            line = " ".join(line)

            if i < len(attendance.presence) - 1:
                line += "\n"

            lines.append(line)

        return lines

    @staticmethod
    def format_to_csv(attendance):
        date = attendance.date.strftime("%d.%m.%Y")

        if len(attendance.students) == 0:
            return [f"Date: {date}"]

        lines = [f"Date: {date}\n"]

        student_structure = ["Name", "Surname", "ID"]

        for i in range(len(attendance.students)):
            student = attendance.students[i].dict(student_structure)

            line = []

            for student_key in student:
                line.append(student[student_key])

            student_id = student["ID"]
            student_presence = "True" if attendance.presence[student_id] else "False"

            line.append(student_presence)

            line = ";".join(line)

            if i < len(attendance.presence) - 1:
                line += "\n"

            lines.append(line)

        return lines