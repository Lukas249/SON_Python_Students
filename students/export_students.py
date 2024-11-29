from file_handler import BaseFileSaver
from students.format_students import BaseFormatStudents
from abc import ABC, abstractmethod

from students.student import Student

class BaseExportStudents(ABC):

    def __init__(self, file_saver: BaseFileSaver, formatter: BaseFormatStudents, export_path: str):
        self.file_saver = file_saver
        self.formatter = formatter
        self.export_path = export_path

    @abstractmethod
    def export(self, students: list[Student]) -> None:
        pass

class ExportStudents(BaseExportStudents):

    def export(self, students: list[Student]) -> None:
        self.file_saver.save(self.export_path, self.formatter.format(students))