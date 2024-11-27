# Input number of students in a class
def numbers_of_student():
    return int(input("Enter number of students: "))
# Input number of courses
def numberofcourse():
    return int(input("Enter number of courses: "))
# Student information input
def student_information():
    return {
        'name': input("Enter student name: "),
        'id': input("Enter student id: "),
        'dob': input("Enter student dob: "),
    }
# Course information
def course_info():
    return {
        'id': input("Enter course's id: "),
        'name': input("Enter course's name: ")
    }
# Mark input
def mark_input(std, courses,course_id):
    for student in std:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        student['marks'][course_id] = mark

# List students
def list_students(std):
    for student in std:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, Date of Birth: {student['dob']}")

# List courses
def list_course(courses):
    for course in courses.values():
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

# List marks
def list_mark(std, course_id):
    for student in std:
        if course_id in student['marks']:
            print(f"Student ID: {student['id']}, Student Name: {student['name']}, Mark: {student['marks'][course_id]}")
        else:
            print(f"Student ID: {student['id']}, Student Name: {student['name']}, Mark: N/A")

# Main function
def main():
    std = []
    courses = {}
    #số lượng sinh viên
    num_students = numbers_of_student()
    for _ in range(num_students):
        student = student_information()
        student['marks'] = {}
        std.append(student)
    #số lượng course
    num_courses = numberofcourse()
    for _ in range(num_courses):
        course = course_info()
        courses[course['id']] = course

    while True:
        print("-----Menu-----")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a given course")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print('Ket thuc chuong trinh')
            break
        elif choice == 1:
            print("-----Courses List-----")
            list_course(courses)
        elif choice == 2:
            print("-----Students List-----")
            list_students(std)
        elif choice == 3:
            course_id = input("Enter course id you need to input mark: ")
            if course_id not in courses:
                print("No such course exists")
                break
            mark_input(std, courses,course_id)
        elif choice == 4:
            course_id2 = input("Enter course id: ")
            list_mark(std, course_id2)

if __name__ == "__main__":
    main()