'''
Student: Jonathan Medina
Date Completed: 9/22/2023
Desc: This program will generate a math quiz tool for elementary first grade students,
each question will be randomized and evaluated, totalling into a final grade at the end
'''
import random
def main():
    count = 0
    letter_grade = ""
    #This for loop will repeat the calculations down below 5 times
    for x in range(5):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, num1)
        #
        '''
        num1 and num2 are the main variables that will be plugged into the randomly generated questions
        it will randomly select a number between 0 and 9 
        '''
        if random.randint(0, 1) == 0:
            question = "What is " + str(num1) + "+" + str(num2) + "="
            correct_answer = num1 + num2
            user_answer = int(input(question))
            if user_answer == correct_answer:
                print("Correct!")
                count += 1
            #the count will add or subtract points depending if the student answered correctly
            else:
                print("Incorrect!")
        else:
            question = "What is " + str(num1) + "-" + str(num2) + "="
            correct_answer = num1 - num2
            user_answer = int(input(question))
            if user_answer == correct_answer:
                print("Correct!")
                count += 1
            else:
                print("Incorrect!")

    #This calculates the total grade by taking total count of points if user enters right
    if count == 5:
        letter_grade = "A"
    elif count == 4:
        letter_grade = "B"
    elif count == 3:
        letter_grade = "C"
    elif count == 2:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("Your final grade is a", letter_grade + "!")

main()


