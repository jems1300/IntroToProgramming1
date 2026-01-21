class Meal:
    def __init__(self):
        self.name = None

    def input_meal(self):
        self.name = input("Enter the meal you want: ")

    def get_meal(self):
        return self.name


class ToGoBox:
    def __init__(self):
        self.customer = None

    def input_name(self):
        self.customer = input("What is the name of the customer?: ")

    def get_name(self):
        return self.customer

    def get_meal(self):
        custom_meal = Meal()
        return custom_meal.get_meal()



class Chef:
    def make_Meal(self):
        shopper = ToGoBox()
        food = Meal()

        food.input_meal()
        shopper.input_name()

        print(f"{shopper.get_name()} ordered {shopper.get_meal()}")

# if __name__ == "__main__":
#     order = input("Enter the meal: ")
#     meal = Meal(order)
#     print(f"The chef has prepared: {meal.get_name()}"
