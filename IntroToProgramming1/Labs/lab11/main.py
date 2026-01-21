'''
Name: Jonathan Medina
Desc: Measures the BMI for two members and determines their class weight
Date Completed: 11/17/2023
'''

from datetime import datetime
#These imports the actual date of today to be used down the line

class Member():
    def __init__(self, name="", year_of_birth=0, weight=0, height=0):
        self.name = name
        self.year_of_birth = year_of_birth
        self.weight = weight
        self.height = height
    #I set name as string and the rest as integers

    def calculate_age(self):
        today = datetime.now().year
        age = today - self.year_of_birth
        return age
    #Now that imported the actual date, I can use it to subtract with the year of birth to get
    #the member's age

    def set_weight(self, new_weight):
        self.weight = new_weight
    #Then as the assignment dictates, in the test file this will prompt the user to update their weight

    def bmi(self):
        weight_kg = self.weight * 0.45359237
        height_meter = self.height * 0.0254
        bmi_value = weight_kg / height_meter ** 2
        return bmi_value
    #I copy pasted the BMI formula from our first assignment earlier this semester and modified it to fit here

    def bmi_class(self):
        bmi_value = self.bmi()
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 25.0:
            return "Normal Weight"
        elif 25.0 <= bmi_value < 30.0:
            return "Overweight"
        elif 30 <= bmi_value:
            return "Obese"
    #I was running into issues using the print function and switched it out with the return function, so they could be
    #called into the test file
