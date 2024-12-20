def list_students(students):
    for student in students:
        print(f"Student ID: {student.student_id}, Student Name: {student.name}, Date of Birth: {student.dob}")

def list_marks(students, course_id):
    for student in students:
        mark = student.get_mark(course_id)
        print(f"Student ID: {student.student_id}, Student Name: {student.name}, Mark: {mark}")

def calculate_and_sort_gpa(students):
    for student in students:
        student.gpa = student.calculate_gpa()
    for student in students:
        print(f"Student ID: {student.student_id}, Student Name: {student.name}, GPA: {student.gpa:.1f}")