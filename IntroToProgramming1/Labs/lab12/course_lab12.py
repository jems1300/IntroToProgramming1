class Course:
    num_of_course = 0

    def __init__(self, course_name="TBA", class_num="TBA", instructor="TBA", students=None):
        self.__course_name = course_name
        self.__class_num = class_num
        self.__instructor = instructor
        self.__students = [] if students is None else students
        Course.increase_course_count()

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, name):
        self.__course_name = name

    def get_class_room(self):
        return self.__class_num

    def set_class_room(self, room):
        self.__class_num = room

    def get_instructor(self):
        return self.__instructor

    def get_students(self):
        return self.__students

    def get_num_of_students(self):
        return len(self.__students)

    def add_students(self, *new_students):
    #After several hours of googling, I found out that adding an * allows me to add another tuple
        for student in new_students:
            student.add_courses(self.__course_name)
            self.__students.append(student)
    #I'll be honest, I still don't understand how this works completely, but it allowed to simplify the test code

    @classmethod
    def increase_course_count(cls):
        cls.num_of_course += 1

    @classmethod
    def get_num_of_courses(cls):
        return cls.num_of_course

