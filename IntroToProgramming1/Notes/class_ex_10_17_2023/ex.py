def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3

    print("The largest number is ", largest)

main()