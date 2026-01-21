def main():
    num = 72
    guess = int(input("Guess the number!"))

    if guess == num:
        print("Correct!")
    elif guess > num:
        print("Too big!")
    elif guess < num:
        print("Too small!")

main()
