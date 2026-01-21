def main():
    minutes = int(input("Enter minutes: "))
    day_to_minutes = 24 * 60

    total_days = minutes // day_to_minutes
    years = total_days // 365
    days = total_days % 365

    print(str(minutes) + " minutes is " + str(years) + " years and " + str(days) + " days")

main()
