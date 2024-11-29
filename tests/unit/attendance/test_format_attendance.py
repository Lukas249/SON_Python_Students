import datetime

from attendance.attendance import Attendance
from attendance.format_attendance import FormatAttendanceCSV, FormatAttendanceTXT
from students.student import Student

class TestFormatAttendance:
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

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024\n",
            "Olivia;Martinez;0OPH46SVQ;False\n",
            "Olivia;Jones;8C32RBB8H;False\n",
            "Sophia;Garcia;MM2BA16UV;False"
        ]

        # When
        got = FormatAttendanceCSV.format(attendance)

        # Then
        assert want == got

    def test_format_to_csv_one_student(self):
        # Given
        students = [
            Student(
                "Olivia",
                "Martinez",
                "0OPH46SVQ"
            ),
        ]

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024\n",
            "Olivia;Martinez;0OPH46SVQ;False",
        ]

        # When
        got = FormatAttendanceCSV.format(attendance)

        # Then
        assert want == got

    def test_format_to_csv_zero_students(self):
        # Given
        students = []

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        want = [
            "Date: 24.11.2024",
        ]

        # When
        got = FormatAttendanceCSV.format(attendance)

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

    def test_format_to_txt_one_student(self):
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

    def test_format_to_txt_zero_students(self):
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