import random
import operator

def quiz():
    score = 0
    for i in range(10):
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!')
            print("Score",(score),"\n")
        else:
            print('Incorrect!')
            print("Score",(score), "\n")

    print('Your score was {}/10'.format(score))


def askQuestion():
    answer = randomCalc()
    guess = float(input())
    return guess == answer

def randomCalc():
    ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv}
    num1 = random.randint(0,11)
    num2 = random.randint(1,11)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?'.format(num1, op, num2))
    return answer

quiz()
#askQuestion()
#randomCalc()