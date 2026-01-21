
def main():
    prices = []
    try:
        while True:
            user_input = float(input("Enter the prices of the items, press 0 to quit at anytime: $"))
            if user_input == 0:
                break
            prices.append(user_input)

        total_num = len(prices)
        total = sum(prices)
        avg_price = total/total_num
        max_price = max(prices)
        min_price = min(prices)

        print("The total number of items is: ", total_num)
        print("The total price is: ", total)
        print("The average price is: ", avg_price)
        print("The maximum price is: ", max_price)
        print("The minimum price is: ", min_price)
    except ValueError:
        print("You cannot input a word or a special character, please try again")
    except ZeroDivisionError:
        print("Your input is invalid, please try again")
main()