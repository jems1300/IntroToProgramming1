'''
Student: Jonathan Medina
Date Completed: 9/19/2023
Desc: This program will calculate the user's total BMI by asking
the user to enter their weight and height
'''
def main():
    #The variables below will prompt the user to enter their weight and height
    weight = float(input("Please enter your weight in lb: "))
    height = float(input("Please enter your height in inches: "))

    weight_in_kg = weight * 0.45359237
    height_in_meters = height * 0.0254
    #taking those inputs, we convert them both into kg anDd meters respectively

    total_BMI = weight_in_kg / (height_in_meters ** 2)
    #to get the total BMI, we divide the weight by the square of the height

    print("Your total BMI is %.2f" %total_BMI)
    #this prompts the final result, the command %.2f will round the number to two decimals

main()