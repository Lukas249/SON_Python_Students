from attendance.parse_attendance import ParseAttendance

class TestParseAttendance:
    def test_parse_to_attendance_csv_multiple_students(self):
        # Given
        lines = [
            "Date: 24.11.2024\n",
            "Olivia;Martinez;0OPH46SVQ;False\n",
            "Olivia;Jones;8C32RBB8H;True\n",
            "Sophia;Garcia;MM2BA16UV;False"
        ]

        want_students = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
            {"Name": "Sophia", "Surname": "Garcia", "ID": "MM2BA16UV"}
        ]

        want_presence = {
            "0OPH46SVQ": False,
            "8C32RBB8H": True,
            "MM2BA16UV": False
        }

        want_date = "24.11.2024"

        # When
        got = ParseAttendance.csv(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_parse_to_attendance_csv_one_student(self):
        # Given
        lines = [
            "Date: 20.11.2024\n",
            "Olivia;Martinez;0OPH46SVQ;True"
        ]

        want_students = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
        ]

        want_presence = {"0OPH46SVQ": True}

        want_date = "20.11.2024"

        # When
        got = ParseAttendance.csv(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_parse_to_attendance_csv_zero_students(self):
        # Given
        lines = [
            "Date: 10.11.2024",
        ]

        want_students = []

        want_presence = {}

        want_date = "10.11.2024"

        # When
        got = ParseAttendance.csv(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")


    def test_format_to_txt_multiple_students(self):
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
        got = ParseAttendance.txt(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_format_to_txt_one_student(self):
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
        got = ParseAttendance.txt(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")

    def test_format_to_txt_zero_students(self):
        # Given
        lines = [
            "Date: 28.12.2023",
        ]

        want_students = []

        want_presence = {}

        want_date = "28.12.2023"

        # When
        got = ParseAttendance.txt(lines)

        # Then
        assert want_students == [student.dict(["Name", "Surname", "ID"]) for student in got.students]
        assert want_presence == got.presence
        assert want_date == got.date.strftime("%d.%m.%Y")