'''
Student: Jonathan Medina
Date Completed: 9/30/2023
Desc: This program will calculate the perimeter of a triangle by taking the inputs of the three faces.
'''

def main():
    isValid = True
    #IsValid is set to true so in case if the numbers don't match up or ar greater than the sum of the parts, it suggests the user to try again

    #the try block statement will automatically catch prompt any variables like letters or special characters and prompt the user to try again, instead of causing a syntax error
    try:
        edge1 = float(input("Enter the 1st edge: "))
        edge2 = float(input("Enter the 2nd edge: "))
        edge3 = float(input("Enter the 3rd edge: "))
        #The variables listed above will prompt the user to enter their selected measurements

        #This makes sure that the perimeter of the triangle isn't exceeding normal measurements, if it does, it will prompt the user to try agian
        if edge1 + edge2 > edge3:
            if edge1 + edge3 > edge2:
                if edge2 + edge3 > edge1:
                    isValid = False
                    perimeter = edge1 + edge2 + edge3
                    print("The perimeter of the triangle is", perimeter)

        if isValid:
            print("Your input is invalid, please try again")

    except Exception:
        print("You may only enter numbers, please try again")

main()