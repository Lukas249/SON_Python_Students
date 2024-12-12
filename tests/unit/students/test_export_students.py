from SON_Python_Students.file_handler import BaseFileSaver
from SON_Python_Students.students.export_students import ExportStudents
from SON_Python_Students.students.format.format_txt_students import FormatStudentsTXT
from SON_Python_Students.students.student import Student

class MockFileSaver(BaseFileSaver):
    path = ""
    lines = []

    def save(self, path: str, lines: list[str]):
        self.path = path
        self.lines = lines

class TestExportStudents:
    def test_export_correct_init(self):
        # Given

        mock_file_saver = MockFileSaver()
        formatter = FormatStudentsTXT()
        export_path = "txt"

        export_students = ExportStudents(
            mock_file_saver,
            formatter,
            export_path
        )

        # Then
        assert export_students.export_path == export_path
        assert export_students.file_saver == mock_file_saver
        assert export_students.formatter == formatter

    def test_export(self):
        # Given

        mock_file_saver = MockFileSaver()
        formatter = FormatStudentsTXT()
        export_path = "txt"

        export_students = ExportStudents(
            mock_file_saver,
            formatter,
            export_path
        )

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

        want_formatted_students = [
            "Olivia Martinez - 0OPH46SVQ\n",
            "Olivia Jones - 8C32RBB8H"
        ]

        # When
        export_students.export(students)

        # Then
        assert mock_file_saver.path == export_path
        assert mock_file_saver.lines == want_formatted_students