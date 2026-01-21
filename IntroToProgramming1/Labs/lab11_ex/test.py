from main import Member

member1 = Member("Alice", 1993, 123, 67)
member2 = Member("Kyle", 1977, 211, 73)

age1 = member1.calculate_age()
new_weight_value1 = float(input("Enter Member's 1 new weight value: "))
member1.set_weight(new_weight_value1)
bmi1 = member1.bmi()
class1 = member1.bmi_class()

age2 = member2.calculate_age()
new_weight_value2 = float(input("Enter Member's 2 new weight value: "))
member2.set_weight(new_weight_value2)
bmi2 = member2.bmi()
class2 = member2.bmi_class()

print(f"{member1.name}'s age is {age1}. Their BMI is {bmi1:.2f} -- {class1}")
print(f"{member2.name}'s age is {age2}. Their BMI is {bmi2:.2f} -- {class2}")