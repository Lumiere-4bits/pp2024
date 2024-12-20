import os
import pickle
from domains.course import Course
from domains.student import Student
from input import * 
from output import *
#compress file
def save_data(students, courses):
    with open('student.pickle', 'wb') as f:
        pickle.dump(students, f)
    with open('course.pickle', 'wb') as f:
        pickle.dump(courses, f)
def load_data():
    student =[]
    courses ={}
    if os.path.exists('student.pickle'):
        with open('student.pickle', 'rb') as file:
            student = pickle.load(file)
        with open('course.pickle', 'rb') as file:
            courses = pickle.load(file)
    return student, courses
def main():
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