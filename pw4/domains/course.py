class Course:
    def __init__(self, course_id, name, credit):
        self.__course_id = course_id
        self.__name = name
        self.__credit = credit

    @property
    def course_id(self):
        return self.__course_id

    @property
    def name(self):
        return self.__name

    @property
    def credit(self):
        return self.__credit