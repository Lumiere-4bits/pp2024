import os
import zipfile
from domains.course import Course
from domains.student import Student
from input import * 
from output import *
#compress file

def main():
    

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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()