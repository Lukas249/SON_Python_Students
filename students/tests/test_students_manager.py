from GitProject.students.student import Student
from GitProject.students.students_manager import StudentsManager

class TestStudentsManager:

    def test_add_student_id_exists(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        new_student = Student(
            "Martinez",
            "Garcia",
            "0OPH46SVQ"
        )

        student_structure = ["Name", "Surname", "ID"]

        want = [student.dict(student_structure) for student in students]

        # When
        manage_students = StudentsManager(students)
        manage_students.add_student(new_student)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want

    def test_add_student_id_not_exist(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        new_student = Student(
            "Martinez",
            "Garcia",
            "ABCABCABC"
        )

        want = [student.dict(student_structure) for student in students]
        want.append(new_student.dict(student_structure))

        # When
        manage_students = StudentsManager(students)
        manage_students.add_student(new_student)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert want == got

    def test_student_exists_when_id_not_exist(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        id = "111"

        want = False

        # When
        manage_students = StudentsManager(students)
        got = manage_students.student_exists(id)

        # Then
        assert got == want

    def test_student_exists_when_id_exists(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        id = "8C32RBB8H"

        want = True

        # When
        manage_students = StudentsManager(students)
        got = manage_students.student_exists(id)

        # Then
        assert got == want

    def test_modify_student_id_not_exist(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        id = "111111111"
        new_student_name = "Sophia"
        new_student_surname = "Garcia"

        want = [student.dict(student_structure) for student in students]

        # When
        manage_students = StudentsManager(students)
        manage_students.modify_student(id, new_student_name, new_student_surname)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want

    def test_modify_student_id_exist(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        id = "0OPH46SVQ"
        new_student_name = "Sophia"
        new_student_surname = "Garcia"

        want = [
            {"Name": "Sophia", "Surname": "Garcia", "ID": "0OPH46SVQ"},
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
            {"Name": "Sophia", "Surname": "Garcia", "ID": "MM2BA16UV"},
        ]

        # When
        manage_students = StudentsManager(students)
        manage_students.modify_student(id, new_student_name, new_student_surname)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want

    def test_delete_first_student_by_id(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        id = "0OPH46SVQ"

        want = [
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
            {"Name": "Sophia", "Surname": "Garcia", "ID": "MM2BA16UV"},
        ]

        # When
        manage_students = StudentsManager(students)
        manage_students.delete_student(id)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want

    def test_delete_last_student_by_id(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
            Student(
                "Olivia",
                "Jones",
                "8C32RBB8H"
            ),
            Student(
                "Sophia",
                "Garcia",
                "MM2BA16UV"
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        id = "MM2BA16UV"

        want = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
        ]

        # When
        manage_students = StudentsManager(students)
        manage_students.delete_student(id)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want