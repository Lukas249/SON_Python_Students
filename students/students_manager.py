from SON_Python_Students.students.export_students import BaseExportStudents
from SON_Python_Students.students.student import Student

class StudentsManager:

    def __init__(self, students: list[Student], exporters: list[BaseExportStudents]):
        self.students = students
        self.exporters = exporters

    def __add(self, student: Student) -> bool:
        if self.student_exists(student.id):
            return False

        self.students.append(student)

        return True

    def add_student(self, student: Student) -> bool:
        student_added = self.__add(student)

        if student_added:
            self.export()

        return student_added

    def student_exists(self, student_id: str) -> bool:
        for student in self.students:
            if student.id == student_id:
                return True

        return False

    def __modify(self, student_id: str, student_name: str, student_surname: str) -> bool:
        if not self.student_exists(student_id):
            return False

        for student in self.students:
            if student.id == student_id:
                student.name = student_name
                student.surname = student_surname

        return True

    def modify_student(self, student_id: str, student_name: str, student_surname: str) -> bool:
        student_modified = self.__modify(student_id, student_name, student_surname)

        if student_modified:
            self.export()

        return student_modified


    def __delete(self, student_id):
        for i in range(len(self.students)):
            if self.students[i].id == student_id:
                del self.students[i]
                return True

        return False

    def delete_student(self, student_id: str) -> bool:
        student_deleted = self.__delete(student_id)

        if student_deleted:
            self.export()

        return student_deleted

    def export(self):
        for exporter in self.exporters:
            exporter.export(self.students)




