def main():
    invalid = True
    """
    Invalid is listed as true, so if the variables below don't meet 
    the requirements, then Invalid will be changed to false, prompting the 
    statement 
    """

    blah = int(input("Please enter a variable"))

    distance = float(input("Please enter commute distance in miles:"))
    daysToSchool = float(input("Please enter commute days in a week:"))
    mpg = float(input("Please enter the MPG:"))
    gasPrice = float(input("Please enter gas price (per gallon):"))
    '''
    These are the same variables used in last week assignment, 
    remaining mostly unchanged, but now with an extra step added below,
    rejecting invalid statements
    '''

    #if each variable is less than or greater than required, it will automatically flag the statement as invalid
    if distance >= 0 and distance <= 100:
        if daysToSchool >= 0 and daysToSchool <= 100:
            if mpg >= 1 and mpg <= 200:
                if gasPrice >= 0 and gasPrice <= 10:
                    invalid = False
                    gasPerTrip = daysToSchool * distance*2 / mpg
                    gasMoneyPerDay = gasPerTrip * gasPrice
                    print("Gas money per week commuting $" + str(gasMoneyPerDay))
    """
    The if statements are grouped together to simplify the process, so if one line doesn't
    meet the criteria, the process is stopped and the invalid statement is prompted up
    """

    if invalid:
        print("Your input is invalid, please try again")

main()