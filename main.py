import datetime

from attendance.attendance import Attendance
from attendance.format_attendance import FormatAttendance
from attendance.parse_attendance import ParseAttendance
from students.format_students import FormatStudents
from students.parse_students import ParseStudents
from file_handler import FileHandler
from students.student import Student
from students.students_manager import StudentsManager

# paths
pathCSV = "lists/student_list.csv"
pathTXT = "lists/student_list.txt"

# import
# students_list = ParseStudents.csv_to_list(FileHandler.load(pathCSV))
students_list = ParseStudents.txt_to_list(FileHandler.load(pathTXT))

'''
for students in lista:
    print(students.get("Name"), students.get("Surname"), students.get("ID"))

'''

'''
for students in lista2:
    print(students.get("Name"), students.get("Surname"), students.get("ID"))
'''

# # students manager
manage_students = StudentsManager(students_list)

#
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

# print all students
# for students in students_list:
#     print(students.name, students.surname, students.id)

# # attendance
# date = datetime.datetime(2024, 11, 24)
# attendance_path = "lists/attendance.txt"
#
# attendance = Attendance(students_list, date)
# attendance.modify_attendance(students_list[0].id, True)
#
# # format attendance
# txt_format_attendance = FormatAttendance.format_to_txt(attendance)
#
# # export attendance
# FileHandler.save(attendance_path, txt_format_attendance)

# # # import and parse attendance
# attendance_path = "lists/attendance.txt"
# attendance = ParseAttendance.txt(FileHandler.load(attendance_path))
#
# print(attendance.date)
# print(attendance.presence)
# print([x.dict(["Name", "Surname", "ID"]) for x in attendance.students])

# # format students
# csv_format_student_list = FormatStudents.format_to_csv(students_list)
# txt_format_student_list = FormatStudents.format_to_txt(students_list)
#
# # export students
# FileHandler.save(pathCSV, csv_format_student_list)
# FileHandler.save(pathTXT, txt_format_student_list)
