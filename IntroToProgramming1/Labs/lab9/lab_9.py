'''
Name: Jonathan Medina
Date Completed: 11/2/2023
Desc: This program goal is to make a loop statement that can give the total price, average price, the number of items
the user inputted, the maximum price and lastly the minimum price depending on what the user puts
'''


def main():
    prices = []

    try:
        while True:
            user_input = float(input("Enter the prices of the items, afterwards press 0 to quit at anytime: $"))
            if user_input == 0:
                break
            #The while true statement can infinitely keep this going until the user decides to quit
            prices.append(user_input)
            #Basically, whatever the user inputs will be added to the list of prices, which is currently empty

        total_num = len(prices)
        #the len function counts how many there is in a list, so if the user put 5 inputs, it counts 5
        total_price = sum(prices)
        avg_price = total_price/total_num
        #To get the average price, I divided the total price with the number of items the user inputted
        max_price = max(prices)
        min_price = min(prices)

        print("The total number of items are: ", total_num)
        print("The total price of the items are: $", total_price)
        print("The average price is: $", avg_price)
        print("The maximum price is: $", max_price)
        print("The minimum price is: $", min_price)

    except ValueError:
        print("You cannot input a word or a special character, please try again and input the price")
    except ZeroDivisionError:
        print("Your input is invalid, please try again")
main()