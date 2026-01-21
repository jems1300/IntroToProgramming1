from main2 import Stock

print("Number of stocks in the system:", Stock.num_of_stocks)
s1 = Stock("ORCL", "Oracle", 34.5, 34.35)
print(s1.name, s1.get_change_percentage(), "%")


s2 = Stock("APPL", "Apple Inc", 189.79, 189.81)
print(s2.name, s2.get_change_percentage(), "%")
print("Number of stocks in the system:", s1.num_of_stocks)


# Stock.num_of_stocks = 10
s2.update_num_of_stocks(20)
print("Num of stocks in the system:", Stock.num_of_stocks)
print("Num of stocks in the system:", s1.num_of_stocks)

print(s1.get_the_date())