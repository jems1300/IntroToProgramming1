'''
Name: Jonathan Medina
Date: 11/9/2023
Desc: Determine how many students opened and closed the lockers
'''

'''
s1 = opens every locker
s2 = begins with the 2nd locker, and close every other locker 
s3 = begins with the 3rd locker and changes every 3rd locker 
s4 = begins with the 4th locker, and changes every 4th locker
s5 = begins with the 5th locker, ad changes every 5th locker
'''

locker = [False] * 100
students = [True] * 100
#I set the lockers to False and students to True

for total_students in range(1, 100):
    for total_locker in range(total_students - 1, 100, total_students):
        #It took me a while to understand this, but I set total students -1 to align properly to the 0 index, and then
        #used total_students again for the other time they would repeat to open a locker (e.g 4th student, so he opens
        #4th locker)
        if students[total_students - 1]:
            locker[total_locker] = not locker[total_locker]
            #locker which is set to false = locker set to true
        #This checks on what the last student did and will inverse depending on the current student (which is always
        #set to True

opened = locker.count(True)
closed = locker.count(False)

for i in range(len(locker)):
    if locker[i - 1]:
        print(f"Locker{i}", end=" ")
#I included the count function to count how many there were opened and closed
print(locker)
print(f"There are {opened} opened lockers")
print(f"There are {closed} closed lockers")
