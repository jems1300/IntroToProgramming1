class Student:
    def __init__(self, first_name="Eren", last_name="Yeager", email="beajaguar@tamusa.edu", courses_registered=None):
        # def __init__(self, first_name="Eren", last_name="Yeager", email="beajaguar@tamusa.edu",courses_registered): <-- This will create an error

        self.__first_name = first_name
        self.__last_name = last_name  # To make it private you put two underscores
        self.__email = email
        self.__courses_registered = courses_registered

    # DON'T FORGET TO PUT SELF OR YOU WILL RUN INTO AN ERROR
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_courses(self):
        return self.__courses_registered

    def add_courses(self, course_name):
        if self.__courses_registered is None:
            self.__courses_registered = [course_name]
        else:
            self.__courses_registered.append(course_name)
        #I am missing something here
