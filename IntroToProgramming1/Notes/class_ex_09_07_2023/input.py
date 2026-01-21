def main():
    weight = float(input("Please enter your weight in lb:"))
    height = float(input("Please enter your height in inches:"))

    weight_in_kg = weight * 0.45359237
    height_in_m = height * 0.0254

    total_bmi = weight_in_kg / (height_in_m ** 2)

    print("Your BMI is", total_bmi)


main()
