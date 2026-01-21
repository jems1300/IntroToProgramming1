from main_lab12 import Student
from course_lab12 import Course

s1 = Student()
s2 = Student("Linda", "Scott", "lin12@gmail.com")
s3 = Student("Jean", "Kirstein", "jean$aot@hotmail.com")
s4 = Student("Jonathan", "Stein", "elihu1301@gmail.com")

c1 = Course(course_name="ENGL 1301", instructor="Dr. Alsmadi")
c2 = Course(course_name="MATH 1324", instructor="Mr. Earwood")
c3 = Course(course_name="MATH 3340", instructor="Dr. Yang")

c1.add_students(s1, s2, s3)
c2.add_students(s1, s2)
c3.add_students(s1, s3)
#Now that I was able to create a tuple from class Course, I can now add students together in a list without having to create multiple lines

print(f"Total number of courses: {Course.num_of_course}")
print(f"{c1.get_course_name()} has {c1.get_num_of_students()} students: {c1.get_students()}")
print(f"{c2.get_course_name()} has {c2.get_num_of_students()} students: {[str(student) for student in c2.get_students()]}")
print(f"{c3.get_course_name()} has {c3.get_num_of_students()} student: {[str(student) for student in c3.get_students()]}")

print(f"{s1.get_first_name()} {s1.get_last_name()} is taking {len(s1.get_courses())} classes: {s1.get_courses()}")
print(f"{s2.get_first_name()} {s2.get_last_name()} is taking {len(s2.get_courses())} classes: {s2.get_courses()}")
print(f"{s3.get_first_name()} {s3.get_last_name()} is taking {len(s3.get_courses())} classes: {s3.get_courses()}")


















