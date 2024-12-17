import math
import numpy as np
class Student:
    def __init__(self, name, student_id, dob):
        self.__name = name
        self.__id = student_id
        self.__dob = dob
        self.__marks = {}

    @property
    def name(self):
        return self.__name
    @property
    def student_id(self):
        return self.__id
    @property
    def dob(self):
        return self.__dob
    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark
    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")
    def list_marks(self):
        return self.__marks
class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name
    @property
    def course_id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
def list_students(students):
    for student in students:
        print(f"Student ID: {student.student_id}, Student Name: {student.name}, Date of Birth: {student.dob}")
def list_courses(courses):
    for course in courses.values():
        print(f"Course ID: {course.course_id}, Course Name: {course.name}")
def input_marks(students, courses):
    course_id = input("Enter course id you need to input mark: ")
    if course_id not in courses:
        print("course doesn't exist")
        return
    for student in students:
        mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
        student.set_mark(course_id, mark)
def list_mark(std, course_id):
    for i in std:
        mark = i.get_mark(course_id)
        print(f"Student ID: {i.student_id}, Student Name: {i.name}, Mark: {mark}")
def GPA(students):
    for student in students:
        student.gpa = student.calculate_gpa()
    for student in students:
        print(f"Student ID: {student.student_id}, Student Name: {student.name}, GPA: {student.gpa:.1f}")

def main():
    num_students = int(input("Enter number of students: "))
    students = []
    for _ in range(num_students):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        students.append(Student(name, student_id, dob))
    courses = {
        "CS101": Course("CS101", "Computer Science", 3),
        "MA101": Course("MA101", "Mathematics", 4)
    }

    while True:
        print("-----Menu-----")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a given course")
        print("5. Calculate and sort GPA")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == 1:
            print("-----Courses List-----")
            list_courses(courses)
        elif choice == 2:
            print("-----Students List-----")
            list_students(students)
        if choice == 3:
            input_marks(students, courses)
        elif choice == 4:
            list_mark(students)
        elif choice == 5:
            GPA(students)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()