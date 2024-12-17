import os
import json
from domains.student import Student
from domains.course import Course

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for _ in range(num_students):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        students.append(Student(name, student_id, dob))
    
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student.student_id},{student.name},{student.dob}\n")
    
    return students

def input_marks(students, courses):
    course_id = input("Enter course id you need to input mark: ")
    if course_id not in courses:
        print("No such course exists")
        return
    with open("marks.txt", "a") as f:
        for student in students:
            mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
            student.set_mark(course_id, mark, courses[course_id].credit)
            f.write(f"{student.student_id},{course_id},{mark}\n")

def input_courses():
    courses = {}
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        courses[course_id] = Course(course_id, name, credit)
    
    with open("courses.txt", "w") as f:
        for course_id, course in courses.items():
            f.write(f"{course.course_id},{course.name},{course.credit}\n")
    
    return courses