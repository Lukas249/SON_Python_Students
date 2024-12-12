from SON_Python_Students.students.student import Student

class TestStudent:
    def test_student(self):
        # Given
        student = Student(
            "Sophia",
            "Garcia",
            "MM2BA16UV"
        )

        assert student.name == "Sophia"
        assert student.surname == "Garcia"
        assert student.id == "MM2BA16UV"

    def test_student_dict(self):
        # Given
        student = Student(
                "John",
                "Garcia",
                "MM2BA16UV"
        )

        student_structure = ["Name", "Surname", "ID"]

        want = {"Name": "John", "Surname": "Garcia", "ID": "MM2BA16UV"}

        # When
        got = student.dict(student_structure)

        # Then
        assert want == got