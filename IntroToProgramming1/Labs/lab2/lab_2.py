def main():
    monthlyDeposit = 0
    AccountBalance = 0
    #these are the main values that the program will use to perform the calculations

    monthly_interest_rate = (1 + 0.00417)/100

    '''''
    as explained in the lab, because the annual interest rate is 5%, 
    you can divide the rate by 12 months which will equal 0.05/12=0.00417
    this is then converted to the monthly_interest_rate variable
    then you can /100 to make it a percentage
    
    BUT WHAT DOES THE 1 DO??
    '''''

    monthlyDeposit = float(input("Please enter your desired deposit amount: $"))
    #user will be prompted to enter their desired deposit amount
    print("Your total account balance for the next 6 months is:")
    #displays the account balance for the next 6 months using the calculations below

    """1st Month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    #this calculates the deposit with the interest rate then adds it to the account balance
    AccountBalance = monthlyDeposit + AccountBalance + interest
    #afterwards it will display the total balance for that month
    print("1st month: $" + str(AccountBalance))

    '''
    this process is repeated onwards for the next 5 months, 
    using the previous AccountBalance variable
    to calculate the next list of instructions 
    '''

    """2nd Month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    AccountBalance = monthlyDeposit + AccountBalance + interest
    print("2nd month: $" + str(AccountBalance))

    """3rd Month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    AccountBalance = monthlyDeposit + AccountBalance + interest
    print("3rd month: $" + str(AccountBalance))

    """4th Month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    AccountBalance = monthlyDeposit + AccountBalance + interest
    print("4th month: $" + str(AccountBalance))

    """5th Month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    AccountBalance = monthlyDeposit + AccountBalance + interest
    print("5th month: $" + str(AccountBalance))

    """6h month"""
    interest = (monthlyDeposit + AccountBalance) * monthly_interest_rate
    AccountBalance = monthlyDeposit + AccountBalance + interest
    print("6th month: $" + str(AccountBalance))

main()