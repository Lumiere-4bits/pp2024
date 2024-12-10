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
def input_mark(students, courses):
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
# Main function
def main():
    std = []
    courses = {}
    #số lượng sinh viên
    num_students = int(input("Enter number of students"))
    for _ in range(num_students):
        print("----------------------------")
        name = input("Enter student's name:")
        dob = input("Enter student's dob:")
        sid = input("Enter student's id:")
        student = Student(name,dob,sid)
        std.append(student)
    #số lượng course
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course's id: ")
        name = input("Enter course's name: ")
        course = Course(course_id, name)
        courses[course.course_id] = course
    while True:
        print("-----Menu-----")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a given course")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print('Program end!')
            break
        elif choice == 1:
            print("-----Courses List-----")
            list_courses(courses)
        elif choice == 2:
            print("-----Students List-----")
            list_students(std)
        elif choice == 3:
            input_mark(std, courses)
        elif choice == 4:
           course_id = input("Enter course id: ")
           list_mark(std, course_id)

if __name__ == "__main__":
    main()