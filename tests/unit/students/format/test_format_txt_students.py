from students.format.format_txt_students import FormatStudentsTXT
from students.student import Student


class TestFormatStudentsTXT:

    def test_format_multiple_students(self):
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
        got = FormatStudentsTXT.format(students)

        # Then
        assert want == got

    def test_format_one_student(self):
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
        got = FormatStudentsTXT.format(students)

        # Then
        assert want == got

    def test_format_zero_students(self):
        # Given
        students = []

        want = []

        # When
        got = FormatStudentsTXT.format(students)

        # Then
        assert want == got