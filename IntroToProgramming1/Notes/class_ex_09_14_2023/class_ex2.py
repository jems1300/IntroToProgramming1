def main():
    month = int(input("Enter a month: "))
    date = int(input("Enter a date: "))

    month_correct = True
    data_correct = True

    if month > 12 or month < 1:
        month_correct = False

    if date > 30 or date < 1:
        data_correct = False

    if month_correct and data_correct:
        print(month, date)

    if month<=12 and month>=1 and date<=30 and date>=1:
        print(month, date)

    if (not month_correct) or (not data_correct):
        print("Invalid date, please try again")


main()