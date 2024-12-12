from datetime import datetime

from SON_Python_Students.students.student import Student

class Attendance:
    def __init__(self, students: list[Student], date: datetime, presence: dict[str, bool] = None):
        self.presence = {x.id: False for x in students} if presence is None else presence
        self.students = students
        self.date = date

    def student_exists(self, student_id: str) -> bool:
        return self.presence.get(student_id, -1) != -1

    def get_attendance(self, student_id: str) -> bool:
        return self.presence.get(student_id, False)

    def modify_attendance(self, student_id: str, is_present: bool) -> bool:
        if not self.student_exists(student_id):
            return False

        self.presence[student_id] = is_present

        return True

    def clear_attendance(self):
        for student_id in self.presence.keys():
            self.presence[student_id] = False