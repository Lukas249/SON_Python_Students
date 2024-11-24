from students.student import Student

class StudentsManager:

    def __init__(self, students: list[Student]):
        self.students = students

    def add_student(self, student: Student) -> bool:
        if self.student_exists(student.id):
            return False

        self.students.append(student)

        return True

    def student_exists(self, student_id: str) -> bool:
        for student in self.students:
            if student.id == student_id:
                return True

        return False

    def modify_student(self, student_id: str, student_name: str, student_surname: str) -> bool:
        if not self.student_exists(student_id):
            return False

        for student in self.students:
            if student.id == student_id:
                student.name = student_name
                student.surname = student_surname

        return True


    def delete_student(self, student_id: str) -> bool:
        for i in range(len(self.students)):
            if self.students[i].id == student_id:
                del self.students[i]
                return True

        return False






