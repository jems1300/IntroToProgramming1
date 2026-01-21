'''
An event management company needs a program to handle the registration of participants. Create a Python program that
allows event organizers to input details for each participant, including their name, age, and registration type.
Once all participant details are entered (by inputting "done"), the program should perform the following tasks:

    1. Calculate the total number of participants registered.
    2. Determine the average age of all participants.
    3. Identify the oldest and youngest participants along with their details (name, age and registration).

Your task is to design a Python program that meets these requirements, allowing organizers to input participant details
and computing statistics based on the entered data.

This problem introduces handling strings for names, integers for ages, and potentially categorical data for registration
types. The objective is to manage these details and calculate statistics from the participant data entered.
'''

# IMPORTANT THIS CODE IS NOT MINE [it has been revised to hell however]
names = []
ages = []
registration_types = []
try:
    while True:
        user_name = input("Enter participant's name (Type 'done' when you are finished): ")
        if user_name.lower() == 'done':
            break
        if user_name.isnumeric():
            print("You cannot input numerical values, please try again")
            continue
        if user_name == #How would I reject special characters like $&#^&?

        try:
            user_age = input("Enter participant's age: ")
            if user_age.lower() == 'done':
                break
            user_age = int(user_age)
            if user_age <= 0 or user_age > 130:
                print("Invalid age, please try again")
                continue
        except ValueError:
            print("Invalid input, please try again")
            continue

        user_registration = input("Enter participant's registration (e.g: Host, Attendant, Employee): ")
        if user_registration.lower() == 'done':
            break
        if user_registration.lower() in ["host", "attendant", "employee"]:
            continue
        else:
            print("Your input is invalid, please try again")
        if user_registration.isnumeric():
            print("You cannot input a numerical value, please try again")
            continue

        names.append(user_name)
        ages.append(user_age)
        registration_types.append(user_registration)

    if len(ages) > 0:
        total_participants = len(names)
        total_age = sum(ages)
        avg_age = total_age / total_participants

        oldest_index = ages.index(max(ages))
        youngest_index = ages.index(min(ages))

        oldest_participants = names[oldest_index]
        oldest_age = ages[oldest_index]
        oldest_registration = registration_types[oldest_index]

        youngest_participants = names[youngest_index]
        youngest_age = ages[youngest_index]
        youngest_registration = registration_types[youngest_index]

        print("The total amount of participants is: ", total_participants)
        print("Participants average age is: ", avg_age)
        print(
            f"The oldest participant is: {oldest_participants} (Age: {oldest_age}) (Registration: {oldest_registration})")
        print(
            f"The youngest participant is: {youngest_participants} (Age: {youngest_age}) (Registration: {youngest_registration})")

    else:
        print("No participant date entered, unable to complete program")
except ValueError:
    print("Your input is invalid, please try again")
