from Student_Main import Student
from Course_Main import Course

s1 = Student()
s2 = Student("Linda", "Scott", "scott120@gmail.com", )

print(Course.get_num_of_courses())
c1 = Course(course_name="ENGL 1301", instructor="Dr. Alsmadi")

c2 = Course(course_name="MATH 1324", instructor="Mr. Earwood")

c3 = Course(course_name="Math 3340", instructor="Dr. Yang")
print(Course.get_num_of_courses())

#register
s2.add_courses(c1.get_course_name())
c1.add_students(s2.get_first_name())

s1.add_courses(c1.get_course_name())
c1.add_students(s1.get_first_name())

print(c1.get_students()[0].set_email("Email"))
# s1.add_courses(c1.get_course_name())
#
# print(s2.get_courses())
# print(s1.get_courses())
#
# s1.add_courses("MATH 1301")
# print(s2.get_courses())
# print(s1.get_courses())