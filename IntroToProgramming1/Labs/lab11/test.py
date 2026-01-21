from main import Member

member1 = Member("Alexa", 1991, 154, 63)
member2 = Member("Jean", 1976, 263, 73)

age1 = member1.calculate_age()
new_weight_value1 = float(input("Please update member 1's new weight: "))
member1.set_weight(new_weight_value1)
bmi1 = member1.bmi()
bmiClass1 = member1.bmi_class()

age2 = member2.calculate_age()
new_weight_value2 = float(input("Please update member 2's new weight: "))
member2.set_weight(new_weight_value2)
bmi2 = member2.bmi()
bmiClass2 = member2.bmi_class()
#These two blocks, now call the main file to calculate the age and BMI

print(f"The BMI for {member1.name} ({age1}) is {bmi1:.2f} -- {bmiClass1}")
print(f"The BMI for {member2.name} ({age2}) is {bmi2:.2f} -- {bmiClass2}")

