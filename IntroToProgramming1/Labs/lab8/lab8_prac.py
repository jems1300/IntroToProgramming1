def disp_double_lines():
    print("||==============================================||")

def main():
    #This is how to do a multiplication table
    disp_double_lines()
    print("||           The Multiplication Table           ||")
    disp_double_lines()



    #This generates the main body
    for row_label in range(1, 11):
        print("|| %-2d |" %(row_label), end="\t")
        for col_label in range(1, 11):
            print(row_label * col_label, end ="\t")
        print("||") #This will start a line breaker
    disp_double_lines()
main()