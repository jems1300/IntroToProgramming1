'''
Student: Jonathan Medina
Date Completed: 9/29/2023
Desc: This program will generate a math quiz tool for elementary first grade students,
each question will be evaluated into a total sum of points at the end of the quiz, whenever
the student decides to finish that is
'''
import random
def main():
    count = 0
    total_count = 0
    connection = ""

    #similar to last week's lab, this will generate a list of random subtraction/addition question
    while True:
    #However one major difference is that 'while True' will generate these questions infinitely, compared to 'for loops' which is finite
        num1 = random.randint(0, 9)
        num2 = random.randint(0, num1)
    #With feedback from another classmate, I substituted num1 in place for the maximum value in num2, this is to prevent negative subtraction questions

        if random.randint (0,1) == 0:
            question = str(num1) + "+" + str(num2) + "="
            user_answer = input(question + "?" + " \nFeel free to quit at any point by typing \"Quit\", otherwise please enter your answer: ")
            if user_answer == "quit" or user_answer == "Quit":
                break
            #If the student decides to quit at any point in the quiz, this will force the program to cease
            user_answer = int(user_answer)
            #otherwise it will take an integer number as suitable answer

            connection = connection + "||" + question + str(num1 + num2)
            #This was inspired by the partial solution example, which displays the questions on the report when finally evaluated

            if user_answer == num1 + num2:
                print("Correct! ✓")
                connection = connection + "\tCorrect!" + "\t||\n"
                total_count += 1
            else:
                print("Incorrect!")
                connection = connection + "\tIncorrect" + "\t||\n"
            count += 1
            #With the addition of connection line, the code from last week's lab remains mostly unchanged

        else:
            question = str(num1) + "-" + str(num2) + "="
            user_answer = input(question + "?" + " \nFeel free to quit at any point by typing \"Quit\", otherwise please enter your answer: ")
            if user_answer == "quit" or user_answer == "Quit":
                break
            user_answer = int(user_answer)

            connection = connection + "||" + question + str(num1 - num2)

            if user_answer == num1 - num2:
                print("Correct! ✓")
                connection = connection + "\tCorrect!" + "\t||\n"
                total_count += 1
            else:
                print("Incorrect!")
                connection = connection + "\tIncorrect!" + "\t||\n"
            count += 1

    print("\n||==============================||")
    print("||             Report           ||")
    print("||==============================||")
    print(connection[:-1])
    print("||======================================||")
    print("||  " + str(total_count) + " out of " + str(count) + " were answered correctly.\t||")
    print("||======================================||")
    '''
    Also inspired by the partial solution example, this report displays all the questions answered correctly/incorrectly 
    and the total sum of points. This was a mix mash of my previous Lab 4 assignment combined with changes needed for Lab 5 
    and some influence from the partial solution example
    '''
main()
