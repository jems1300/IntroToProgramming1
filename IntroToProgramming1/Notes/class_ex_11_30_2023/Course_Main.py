class Course:
    num_of_course = 0

    def __init__(self, course_name="TBA", class_room="TBA", instructor="TBA", students=None):
        self.__course_name = course_name
        self.__class_room = class_room
        self.__instructor = instructor
        self.__students = students
        Course.increase_course_count()
        # if it's

    def get_course_name(self):
        return self.__course_name

    def get_num_of_students(self):
        return len(self.__students)

    def get_students(self):
        return self.__students

    def add_students(self, student):
        # input is a Student object
        if self.__students is None:
            self.__students = [student]
        else:
            self.__students.append(student)

    @classmethod
    def increase_course_count(cls):
        cls.num_of_course += 1

    @classmethod
    def get_num_of_courses(cls):
        return cls.num_of_course
