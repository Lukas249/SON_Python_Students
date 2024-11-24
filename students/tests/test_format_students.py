from GitProject.students.format_students import FormatStudents
from GitProject.students.student import Student


class TestFormatStudents:
    def test_format_to_csv_multiple_students(self):
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

        want = [
            "Olivia;Martinez;0OPH46SVQ\n",
            "Olivia;Jones;8C32RBB8H\n",
            "Sophia;Garcia;MM2BA16UV"
        ]

        # When
        got = FormatStudents.format_to_csv(students)

        # Then
        assert want == got

    def test_format_to_csv_one_student(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            )
        ]

        want = [
            "Olivia;Martinez;0OPH46SVQ",
        ]

        # When
        got = FormatStudents.format_to_csv(students)

        # Then
        assert want == got

    def test_format_to_csv_zero_students(self):
        # Given
        students = []

        want = []

        # When
        got = FormatStudents.format_to_csv(students)

        # Then
        assert want == got

    def test_format_to_txt_multiple_students(self):
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

        want = [
            "Olivia Martinez - 0OPH46SVQ\n",
            "Olivia Jones - 8C32RBB8H\n",
            "Sophia Garcia - MM2BA16UV"
        ]

        # When
        got = FormatStudents.format_to_txt(students)

        # Then
        assert want == got

    def test_format_to_txt_one_student(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            )
        ]

        want = [
            "Olivia Martinez - 0OPH46SVQ",
        ]

        # When
        got = FormatStudents.format_to_txt(students)

        # Then
        assert want == got

    def test_format_to_txt_zero_students(self):
        # Given
        students = []

        want = []

        # When
        got = FormatStudents.format_to_txt(students)

        # Then
        assert want == got