from students.parse.parse_txt_students import ParseStudentsTXT


class TestParseStudentsTXT:

    def test_parse_multiple_students(self):
        # Given
        file_content = [
            "Olivia Martinez - 0OPH46SVQ\n",
            "Olivia Jones - 8C32RBB8H\n",
            "Sophia Garcia - MM2BA16UV",
        ]

        student_structure = ["Name", "Surname", "ID"]

        want = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
            {"Name": "Olivia", "Surname": "Jones", "ID": "8C32RBB8H"},
            {"Name": "Sophia", "Surname": "Garcia", "ID": "MM2BA16UV"},
        ]

        # When
        got = [student.dict(student_structure) for student in ParseStudentsTXT.parse(file_content)]

        # Then
        assert want == got

    def test_parse_one_student(self):
        # Given
        file_content = [
            "Olivia Martinez - 0OPH46SVQ",
        ]

        student_structure = ["Name", "Surname", "ID"]

        want = [
            {"Name": "Olivia", "Surname": "Martinez", "ID": "0OPH46SVQ"},
        ]

        # When
        got = [student.dict(student_structure) for student in ParseStudentsTXT.parse(file_content)]

        # Then
        assert want == got

    def test_parse_zero_students(self):
        # Given
        file_content = []

        student_structure = ["Name", "Surname", "ID"]

        want = []

        # When
        got = [student.dict(student_structure) for student in ParseStudentsTXT.parse(file_content)]

        # Then
        assert want == got