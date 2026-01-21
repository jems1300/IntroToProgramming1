class Student:
    def __init__(self, first_name="Eren", last_name="Yeager", email="rumbling12@gmail.com", courses_registered=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__courses_registered = courses_registered

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    #In the test we can add len to get the number of classes
    def get_courses(self):
        return self.__courses_registered

    def add_courses(self, course_name):
        if self.__courses_registered is None:
            self.__courses_registered = [course_name]
            #What does it when it equals = [course_name]? Is it saying that course name will be in an empty list
        else:
            self.__courses_registered.append(course_name)

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"


