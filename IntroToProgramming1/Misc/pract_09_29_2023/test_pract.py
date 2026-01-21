import random
def main():
    count = 0
    total_count = 0

    while True:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, num1)

        if random.randint (0,1) == 0:
            question = "What is " + str(num1) + "+" + str(num2) + "="
            user_answer = input(question + "?" + " Feel free to quit at any point by typing \"Quit\".")
            if user_answer == "quit" or user_answer == "Quit":
                break
            user_answer = int(user_answer)

            if user_answer == num1 + num2:
                print("Correct!")
                total_count += 1
            else:
                print("Incorrect!")

            count += 1

        else:
            question = "What is " + str(num1) + "-" + str(num2) + "="
            user_answer = input(question + "?" + " Feel free to quit at any point by typing \"Quit\".")
            if user_answer == "quit" or user_answer == "Quit":
                break
            user_answer = int(user_answer)

            if user_answer == num1 - num2:
                print("Correct!")
                total_count += 1
            else:
                print("Incorrect!")

            count += 1


main()
