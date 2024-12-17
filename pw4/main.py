from domains.course import Course
from input import *
from output import *

def main():
    students = input_students()

    courses = {
        "CS101": Course("CS101", "Computer Science", 3),
        "MA101": Course("MA101", "Mathematics", 4)
    }

    while True:
        print("1. Input marks")
        print("2. List students")
        print("3. Calculate and sort GPA")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            input_marks(students, courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            calculate_and_sort_gpa(students)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()