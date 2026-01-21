"""
Write the definition of a Class Counter containing:
- An int instance variable counter, and an int instance variable 'limit'
- A constructor that takes two int argument and assigns the first value to counter and the first value to limit
- A method called increment that adds one to the instance variable counter if counter is less than limit.
This doesn't accept parameters or return a value
- A method called decrement that subtracts one to the instance variable counter if counter is greater than 0. This
doesn't accept parameters or return a value
- A method called get_value that doesn't accept any parameters. It returns the value of the instance variable counter
"""

class Counter():
    def __init__(self, counter = 0, limit=5):
        self.counter = counter
        self.limit = limit

    def increment(self):
        if self.counter < self.limit:
            self.counter += 1

    def decrement(self):
        if self.counter > self.limit:
            self.counter -= 1

    def get_value(self):
        return self.counter

    #I have a lot of questions

"----------------------------------------------------------------------------------------------------------------------"

class Player():
    def __int__(self, name="", score=0):
        self.name = name
        self.score = score

    def set_name(self, name):
        self.name = name #

    def set_score(self, score):
        if self.score + score >40:
            self.score = score
        else:
            print("The score is wrong!")

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score


#Teacher's example, write this in another py file then import this Class
#from Player import Player

#def show_player_info(player):
#   print(player.get_name(), player.score)
#
#p1 = Player(name: "Mr P", score:0)
#p1.set_name("Peter Lee")
#p1.score = 30

#p2 = Player(name: "Carol Burt", score: 40) [[[[[[[[[[[[[[[[[[[[[[d