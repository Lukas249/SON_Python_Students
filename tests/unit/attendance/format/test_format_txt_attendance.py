import datetime

from attendance.attendance import Attendance
from attendance.format.format_txt_attendance import FormatAttendanceTXT
from students.student import Student

class TestFormatAttendanceTXT:
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

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024\n",
            "Olivia Martinez - 0OPH46SVQ False\n",
            "Olivia Jones - 8C32RBB8H False\n",
            "Sophia Garcia - MM2BA16UV False"
        ]

        # When
        got = FormatAttendanceTXT.format(attendance)

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

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024\n",
            "Olivia Martinez - 0OPH46SVQ False",
        ]

        # When
        got = FormatAttendanceTXT.format(attendance)

        # Then
        assert want == got

    def test_format_zero_students(self):
        # Given
        students = []

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024",
        ]

        # When
        got = FormatAttendanceTXT.format(attendance)

        # Then
        assert want == got