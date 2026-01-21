from datetime import date


class Stock:
    num_of_stocks = 0  # Class variable

    def __init__(self, symbol, name, prev_price, curr_price):
        self.symbol = symbol
        self.name = name
        self.prev_price = prev_price
        self.curr_price = curr_price

        Stock.num_of_stocks += 1

    def get_change_percentage(self):
        return ((self.curr_price - self.prev_price) / self.prev_price) * 100


    @classmethod  # <-- What does this mean?
    def update_num_of_stocks(cls, num_of_stocks):
        cls.num_of_stocks = num_of_stocks

    @staticmethod
    def get_the_date():
        return date.today()
