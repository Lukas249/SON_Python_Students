import datetime

from GitProject.attendance.attendance import Attendance
from GitProject.students.student import Student


class TestAttendance:
    def test_attendance(self):
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

        presence = {
            "0OPH46SVQ": False,
            "8C32RBB8H": False,
            "MM2BA16UV": False
        }

        # Then
        assert attendance.date == date
        assert attendance.students == students
        assert attendance.presence == presence

    def test_get_attendance_id_not_exist(self):
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

        id = "12345"

        want = False

        # When
        got = attendance.get_attendance(id)

        # Then
        assert got == want

    def test_get_attendance(self):
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

        id = "MM2BA16UV"

        want = False

        # When
        got = attendance.get_attendance(id)

        # Then
        assert got == want

    def test_get_attendance_student_present(self):
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

        id = "MM2BA16UV"

        want = True

        # When
        attendance.modify_attendance(id, True)
        got = attendance.get_attendance(id)

        # Then
        assert got == want

    def test_modify_attendance_student_present(self):
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

        id = "MM2BA16UV"

        want = True

        # When
        attendance.modify_attendance(id, True)
        got = attendance.get_attendance(id)

        # Then
        assert got == want

    def test_modify_attendance_student_not_present(self):
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

        id = "MM2BA16UV"

        want = False

        # When
        attendance.modify_attendance(id, False)
        got = attendance.get_attendance(id)

        # Then
        assert got == want

    def test_modify_attendance_multiple_students_present(self):
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

        want = {
            "0OPH46SVQ": True,
            "8C32RBB8H": False,
            "MM2BA16UV": True
        }

        # When
        attendance.modify_attendance("0OPH46SVQ", True)
        attendance.modify_attendance("MM2BA16UV", True)

        got = attendance.presence

        # Then
        assert got == want

    def test_modify_attendance_id_not_exist(self):
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

        id = "12345"

        want = False

        # When
        got = attendance.modify_attendance(id, True)

        # Then
        assert got == want

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

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        id = "12345"

        want = False

        # When
        got = attendance.student_exists(id)

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

        date = datetime.datetime(2024, 11, 24)
        attendance = Attendance(students, date)

        id = "MM2BA16UV"

        want = True

        # When
        got = attendance.student_exists(id)

        # Then
        assert got == want

    def test_clear_attendance(self):
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

        want = {
            "0OPH46SVQ": False,
            "8C32RBB8H": False,
            "MM2BA16UV": False
        }

        # When
        attendance.modify_attendance("0OPH46SVQ", True)
        attendance.modify_attendance("MM2BA16UV", True)

        attendance.clear_attendance()

        got = attendance.presence

        # Then
        assert got == want