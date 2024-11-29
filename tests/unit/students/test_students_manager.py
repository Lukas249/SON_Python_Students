from file_handler import BaseFileSaver
from students.export_students import BaseExportStudents
from students.format_students import FormatStudentsTXT, FormatStudentsCSV
from students.student import Student
from students.students_manager import StudentsManager


class MockExportStudents(BaseExportStudents):
    export_data = []

    def export(self, students: list[Student]) -> None:
        self.export_data = students

class MockFileSaver(BaseFileSaver):
    path = ""
    lines = []

    def save(self, path: str, lines: list[str]):
        self.path = path
        self.lines = lines

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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
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

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path=""
        )
        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.delete_student(id)

        got = [student.dict(student_structure) for student in manage_students.students]

        # Then
        assert got == want

    def test_export_after_delete_student(self):
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
            {
                "Name": "Olivia",
                "Surname": "Martinez",
                "ID": "0OPH46SVQ",
            },
            {
                "Name": "Olivia",
                "Surname": "Jones",
                "ID": "8C32RBB8H"
            }
        ]

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path="txt"
        )
        exporter_csv = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsCSV(),
            export_path="csv"
        )

        exporters = [exporter_txt, exporter_csv]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.delete_student(id)

        got_exporter_txt = [student.dict(student_structure) for student in exporter_txt.export_data]
        got_exporter_csv = [student.dict(student_structure) for student in exporter_csv.export_data]

        # Then
        assert got_exporter_txt == want
        assert got_exporter_csv == want

    def test_export_after_add_student(self):
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
            )
        ]

        new_student = Student(
            "Sophia",
            "Garcia",
            "MM2BA16UV"
        )

        student_structure = ["Name", "Surname", "ID"]

        want = [
            {
                "Name": "Olivia",
                "Surname": "Martinez",
                "ID": "0OPH46SVQ",
            },
            {
                "Name": "Olivia",
                "Surname": "Jones",
                "ID": "8C32RBB8H"
            },
            {
                "Name": "Sophia",
                "Surname": "Garcia",
                "ID": "MM2BA16UV"
            }
        ]

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path="txt"
        )
        exporter_csv = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsCSV(),
            export_path="csv"
        )

        exporters = [exporter_txt, exporter_csv]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.add_student(new_student)

        got_exporter_txt = [student.dict(student_structure) for student in exporter_txt.export_data]
        got_exporter_csv = [student.dict(student_structure) for student in exporter_csv.export_data]

        # Then
        assert got_exporter_txt == want
        assert got_exporter_csv == want

    def test_export_after_modify_student(self):
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
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        id = "8C32RBB8H"
        new_name = "Sophia"
        new_surname = "Garcia"

        want = [
            {
                "Name": "Olivia",
                "Surname": "Martinez",
                "ID": "0OPH46SVQ",
            },
            {
                "Name": "Sophia",
                "Surname": "Garcia",
                "ID": "8C32RBB8H"
            }
        ]

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path="txt"
        )
        exporter_csv = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsCSV(),
            export_path="csv"
        )

        exporters = [exporter_txt, exporter_csv]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.modify_student(id, new_name, new_surname)

        got_exporter_txt = [student.dict(student_structure) for student in exporter_txt.export_data]
        got_exporter_csv = [student.dict(student_structure) for student in exporter_csv.export_data]

        # Then
        assert got_exporter_txt == want
        assert got_exporter_csv == want

    def test_export_with_zero_exporters(self):
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
            )
        ]

        exporters = []

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.export()

    def test_export_with_one_exporter(self):
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
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        want = [
            {
                "Name": "Olivia",
                "Surname": "Martinez",
                "ID": "0OPH46SVQ",
            },
            {
                "Name": "Olivia",
                "Surname": "Jones",
                "ID": "8C32RBB8H"
            }
        ]

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path="txt"
        )

        exporters = [exporter_txt]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.export()

        got_exporter_txt = [student.dict(student_structure) for student in exporter_txt.export_data]

        # Then
        assert got_exporter_txt == want

    def test_export_with_multiple_exporters(self):
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
            )
        ]

        student_structure = ["Name", "Surname", "ID"]

        want = [
            {
                "Name": "Olivia",
                "Surname": "Martinez",
                "ID": "0OPH46SVQ",
            },
            {
                "Name": "Olivia",
                "Surname": "Jones",
                "ID": "8C32RBB8H"
            }
        ]

        exporter_txt = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsTXT(),
            export_path="txt"
        )
        exporter_csv = MockExportStudents(
            file_saver=MockFileSaver(),
            formatter=FormatStudentsCSV(),
            export_path="csv"
        )

        exporters = [exporter_txt, exporter_csv]

        # When
        manage_students = StudentsManager(students, exporters)
        manage_students.export()

        got_exporter_txt = [student.dict(student_structure) for student in exporter_txt.export_data]
        got_exporter_csv = [student.dict(student_structure) for student in exporter_csv.export_data]

        # Then
        assert got_exporter_txt == want
        assert got_exporter_csv == want