import random
def main():
    count = 0
    for i in range(5):
        correct_answer = userAnswer()
        if correct_answer:
            count += 1
            print("Great job!")
        else:
            print("Incorrect!")

def userAnswer():
    ops = {'+': operator.add,'-': operator.sub}
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    print('What is {} {} {}?'.format(num1, op, num2))
    return answer


main()