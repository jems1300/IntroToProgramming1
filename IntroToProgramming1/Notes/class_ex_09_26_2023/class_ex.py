import random
def main():
    rand_num = random.randint(0, 9)
    count = 0
    continue_to_play = True

    while count < 10:
        guess = int(input("Guess between 0 and 9: "))

        if guess == rand_num:
            print("Nice!")
            continue_to_play = False
        elif guess < rand_num:
            print("Seriously? Too small!")
        else:
            print("TOO BIG!")

        count += 1




main()