import math
import numpy as np

class Student:
    def __init__(self, name, student_id, dob):
        self.__name = name
        self.__id = student_id
        self.__dob = dob
        self.__marks = {}
        self.__credits = {}

    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__id

    @property
    def dob(self):
        return self.__dob

    def set_mark(self, course_id, mark, credit):
        self.__marks[course_id] = math.floor(mark * 10) / 10
        self.__credits[course_id] = credit

    def get_mark(self, course_id):
        return self.__marks.get(course_id, "N/A")

    def calculate_gpa(self):
        total_credits = sum(self.__credits.values())
        weighted_sum = sum(np.array(list(self.__marks.values())) * np.array(list(self.__credits.values())))
        return weighted_sum / total_credits if total_credits != 0 else 0