import random


def main():
    count = 0  # total questions
    correct_count = 0  # number of questions got correct

    min_value = 0
    max_value = 10

    s = ""  # an string for all questions

    while True:
        num1 = random.randint(min_value, max_value)
        num2 = random.randint(min_value, max_value)

        if num1 < num2:
            temp = num1
            num1 = num2
            num2 = temp

        question = str(num1) + " - " + str(num2) + " = "
        answer = input(question + "?" + " Enter \"quit\" to quit the quiz.")  # read input as a str
        if answer == "quit" or answer == "Quit":
            break
        answer = int(answer)

        s = s + "||    " + question + str(num1 - num2)

        if answer == num1 - num2:
            print("Great job! ")
            s = s + "\tCorrect" + "\t||\n"
            correct_count += 1  # increase correct count
        else:
            print("Wrong answer")
            s = s + "\tWrong" + "\t||\n"

        count += 1  # increase total count

    # Display the report
    print("\n||==============================||")
    print("||             Report           ||")
    print("||==============================||")
    print(s[:-1])  # remove the last line breaker
    print("||==============================||")
    print("||  " + str(correct_count) + " out of " + str(count) + " were correct.\t||")
    print("||==============================||")


main()

