import os
import zipfile
from domains.course import Course
from domains.student import Student
from input import * 
from output import *
#compress file
def compress_files():
    with zipfile.ZipFile('students.dat', 'w') as zipf:
        for file in ['students.txt', 'courses.txt', 'marks.txt']:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def decompress_files():
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()

def load_data():
    students = []
    courses = {}
    if os.path.exists('students.txt'):
        with open('students.txt', 'r') as f:
            for line in f:
                student_id, name, dob = line.strip().split(',')
                students.append(Student(name, student_id, dob))
    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r') as f:
            for line in f:
                course_id, name, credit = line.strip().split(',')
                courses[course_id] = Course(course_id, name, int(credit))
    if os.path.exists('marks.txt'):
        with open('marks.txt', 'r') as f:
            for line in f:
                student_id, course_id, mark = line.strip().split(',')
                for student in students:
                    if student.student_id == student_id:
                        student.set_mark(course_id, float(mark), courses[course_id].credit)
    return students, courses

def main():
    decompress_files()
    students, courses = load_data()
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. Calculate and sort GPA")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            students = input_students()
        elif choice == '2':
            courses = input_courses()
        elif choice == '3':
            input_marks(students, courses)
        elif choice == '4':
            list_students(students)
        elif choice == '5':
            calculate_and_sort_gpa(students)
        elif choice == '6':
            compress_files()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()