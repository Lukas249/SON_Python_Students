from attendance.parse.parse_txt_attendance import ParseAttendanceTXT


class TestParseAttendanceTXT:

    def test_parse_multiple_students(self):
        # Given
        lines = [
            "Date: 26.12.2023\n",
            "Olivia Martinez - 0OPH46SVQ False\n",
            "Olivia Jones - 8C32RBB8H False\n",
            "Sophia Garcia - MM2BA16UV True"
        ]

        want_students = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
            {"Name": "Sophia", "Surname": "Garcia", "ID": "MM2BA16UV"}
        ]

        want_presence = {
            "0OPH46SVQ": False,
            "8C32RBB8H": False,
            "MM2BA16UV": True
        }

        want_date = "26.12.2023"

        # When
        got = ParseAttendanceTXT.parse(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_parse_one_student(self):
        # Given
        lines = [
            "Date: 28.12.2023\n",
            "Olivia Martinez - 0OPH46SVQ False",
        ]

        want_students = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
        ]

        want_presence = {
            "0OPH46SVQ": False
        }

        want_date = "28.12.2023"

        # When
        got = ParseAttendanceTXT.parse(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_parse_zero_students(self):
        # Given
        lines = [
            "Date: 28.12.2023",
        ]

        want_students = []

        want_presence = {}

        want_date = "28.12.2023"

        # When
        got = ParseAttendanceTXT.parse(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")