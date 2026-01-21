"""
Suppose that you are working at the university registrar’s office. To evaluate students’ performance,
you need to know the average GPA of all students and the number of students whose GPA is above the average
Write a program that can do this, but to make the task simpler, we assume the university only has 100 students.
So, can you write a program that reads 100 floating-point numbers from the user, compute their average, and find out
how many numbers are above the average
"""


#def main():
#    #Find the average GPA of students
#    sum = 0
#    for i in range(5):
#        sum += float(input("Enter a GPA: "))
#    average_gpa = sum/5

#    #Find the number of students whose GPA is greater than the average GPA
#    for i in range(5):
#        gpa = float(input("Enter a GPA: "))
#        if gpa > average_gpa:
#            count += 1

#main()

#Let user to enter all GPAs and store them. Compute the average from the stored GPA, and use stored GPA and average to
#out the # of students

#gpa_list = []
#for i in range(5):
    #gpa_list.insert(len(gpa_list), float(input("Enter a GPA: ")))
    #print(gpa_list)

#compute the average, traverse the list
#print(sum(gpa_list))
#for i in range(5):
#    print(gpa_list[i])
#for i in range (5):
#    print(gpa_list[i])

#for i in gpa_list:
#    print(i)


#average_gpa = sum(gpa_list) / len(gpa_list)

#################################################
gpa_list = []
for i in range(5):
    gpa_list.insert(len(gpa_list), float(input("Enter a GPA: ")))
    print(gpa_list)

average_gpa = sum(gpa_list)/len(gpa_list)
average_gpa = ((average_gpa*100)//1)/100
#Find out the # of students GPA that is greater than the average and traverse the list
count = 0
for i in range(len(gpa_list)):
    if gpa_list[i] > average_gpa:
        count += 1

print("all gpas:", gpa_list)
print("average gpa: %2f" %average_gpa)
print("# of students' GPA > ave:", count)