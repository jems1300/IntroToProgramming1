from datetime import datetime


class Member():
    def __init__(self, name="", year_of_birth=0, weight=0, height=0):
        self.name = name
        self.year_of_birth = year_of_birth
        self.weight = weight
        self.height = height

    def calculate_age(self):
        today = datetime.now().year
        age = today - self.year_of_birth
        return age

    def set_weight(self, new_weight):
        self.weight = new_weight

    def bmi(self):
        weight_kg = self.weight * 0.45359237
        height_meter = self.height * 0.0254
        bmi_value = (weight_kg / height_meter ** 2)
        return bmi_value

    def bmi_class(self):
        bmi_value = self.bmi()
        if bmi_value < 18.5:
            return "Underweight"
        elif 18.5 <= bmi_value < 25:
            return "Normal weight"
        elif 25.0 <= bmi_value < 30.0:
            return "Overweight"
        elif 30.0 <= bmi_value:
            return "Obese"


