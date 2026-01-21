def foo(row):
    for i in range(0, row, 1):
        for j in range(0, row-i-1, 1):
            print("   ", end="")
        for j in range(0, i*2+1, 1):
            print("x  ", end="")
        print("hello")
foo(5)

def getSumInt (start, end):
    sum = 0
    for i in range(start, end+1, 1):
        sum += i
    print("The sum between %d and %d is %d" %(start, end, sum))

getSumInt(0, 10)
getSumInt(100, 256)

#high level idea for functions
