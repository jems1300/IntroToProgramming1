def main():
    #while loop version
    count = 0
    while count < 100:
        print("Hello Jaguars!")
        count += 1

    #for loop version
    for i in range(100):
        print("Hello Jaguars!")

    #another for-loop example
    sum = 0
    for item in range(0, 10, 1):
        sum += item
        print(item)

    # Write a program to calculate the sum of the odd numbers between 1 and 100
    sum = 0
    for item in range(1, 100, 2):
        sum += item
        print(item)

    '''
    Personally I prefer the for loop version, much simpler to work with
    '''

    '''
    Write a program to generate a table of a power of 2
    The table has two columns, the 1st column is an integer, and the 2nd column
    shows the value of 2 raised to the power of that integer
    '''

    for item in range(0, 10, 1):
        p = 2 ** item
        print(item, "\t", p)
    # A simpler way to write this

    #outer loop
    for i in range(3):
        #inner loop
            for j in range(3):
                print("i=%d, k=%d" % (i, j))

    for i in range(0, 2, 1):
        for j in range(0, 2, 1):
            print("i=%d, j=%d" %(1, j))
            break #It will only break the loop that is closests

    def main():
        for i in range(0, 100, 1):  # 2
            for j in range(0, 100, 1):  # 2
                for k in range(0, 100, 1): 2
                print("i=%d, j=%d, k=%d" % (i, j, k))

        # for i in range(0, 5, 1): #contorl the number of rows
        # for j in range(0, i, 1): #i-1, (0,3,1)
        # print("- ", end ="")
        # for j in range(0, 5-i, 1): #(0,2,1)
        # print("* ", end="")
        # print()
        row = 3
        for i in range(0, row, 1):
            for j in range(0, i + 1, 1):
                print("  ", end="")
            for j in range(0, row - i, 1):
                print("*  ", end="")
            print()


main()