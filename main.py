import datetime

from attendance.attendance import Attendance
from attendance.format_attendance import FormatAttendanceTXT
from attendance.parse_attendance import ParseAttendanceTXT
from students.export_students import ExportStudents
from students.format_students import FormatStudentsTXT, FormatStudentsCSV
from students.parse_students import ParseStudentsTXT, ParseStudentsCSV
from file_handler import FileHandler
from students.student import Student
from students.students_manager import StudentsManager

# paths
pathCSV = "lists/student_list.csv"
pathTXT = "lists/student_list.txt"

# import
# students_list = ParseStudentsCSV.parse(FileHandler.load(pathCSV))
students_list = ParseStudentsTXT.parse(FileHandler.load(pathTXT))


# for students in students_list:
#     print(students.name, students.surname, students.id)

'''
for students in lista2:
    print(students.get("Name"), students.get("Surname"), students.get("ID"))
'''

# # students manager
# students_txt_exporter = ExportStudents(
#     file_saver=FileHandler(),
#     formatter=FormatStudentsTXT(),
#     export_path=pathTXT
# )
#
# students_csv_exporter = ExportStudents(
#     file_saver=FileHandler(),
#     formatter=FormatStudentsCSV(),
#     export_path=pathCSV
# )
#
# manage_students = StudentsManager(students_list, [students_txt_exporter, students_csv_exporter])


# # add students
# new_student = Student(
#     input("Enter students's name: "),
#     input("Enter students's surname: "),
#     input("Enter students's ID: ")
# )
#
# manage_students.add_student(new_student)

# modify students data
# modified_student = {
#   "ID": input("Enter students's ID to modify: "),
#   "Name": input("Enter new students's name: "),
#   "Surname": input("Enter new students's surname: "),
# }
# manage_students.modify_student(modified_student.get("ID"), modified_student.get("Name"), modified_student.get("Surname"))

# delete students
# student_id_to_delete = input("Enter students's ID to delete: ")
# manage_students.delete_student(student_id_to_delete)

# attendance
# date = datetime.datetime(2024, 11, 24)
# attendance_path = "lists/attendance.txt"
#
# attendance = Attendance(students_list, date)
# attendance.modify_attendance(students_list[0].id, True)
#
# # format attendance
# txt_format_attendance = FormatAttendanceTXT.format(attendance)
#
# # export attendance
# FileHandler.save(attendance_path, txt_format_attendance)
#
# # # import and parse attendance
# attendance_path = "lists/attendance.txt"
# attendance = ParseAttendanceTXT.parse(FileHandler.load(attendance_path))
#
# print(attendance.date)
# print(attendance.presence)
# print([x.dict(["Name", "Surname", "ID"]) for x in attendance.students])
