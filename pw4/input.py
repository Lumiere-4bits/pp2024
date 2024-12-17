from domains.student import Student

def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    for _ in range(num_students):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        dob = input("Enter student date of birth: ")
        students.append(Student(name, student_id, dob))
    return students

def input_marks(students, courses):
    course_id = input("Enter course id you need to input mark: ")
    if course_id not in courses:
        print("No such course exists")
        return
    for student in students:
        mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
        student.set_mark(course_id, mark, courses[course_id].credit)