#The main is a function!
import random
def main():
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    if num1<num2:
        temp = num1
        num1 = num2
        num2 = temp

    answer = -1
    while( not (answer == (num1-num2)) ):
        print("What is %d-%d " %(num1, num2))
        answer = int(input())
    print("Good job")
main()

