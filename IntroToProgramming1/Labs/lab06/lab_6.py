'''
Student Name: Jonathan Medina
Date Completed: October 6th, 2023
Desc: This is a program simulating rock, paper and scissors game, where each input value is taken
account of and where the computer also gets to randomly decided what to pick as the opponent
'''

import random
def main():
    print("Welcome to rock, paper and scissors! Feel free to quit at any point by typing 'Quit'")

    while True:
        possible_outputs = ["rock", "paper", "scissors"]
        #Above are the three given possibilies the game will be conducted on, and that player two will follow from
        computer = random.choice(possible_outputs)
        #inserting those possible outputs into the random choice generator, the computer again will be able to draw from that list
        rps_input = input("Try your luck! Enter either rock, paper, or scissors: ")
        rps_input = rps_input.lower()
        #Regardless if they type in lower case or upper case letters, the program will recognize the words and accept it
        if rps_input == "quit":
            break

    #Below is the if statements I've come up with regarding on how the program determines who is the loser and winner
        print("Player 2 chose", computer)
        if rps_input == computer:
            print("It's a tie!")
        elif rps_input == "rock":
            if computer == "paper":
                print("Paper beats rock, you lose!")
            if computer == "scissors":
                print("Rocks beats scissors, you win!")
        elif rps_input == "paper":
            if computer == "rock":
                print("Paper beats rock, you win!")
            if computer == "scissors":
                print("Scissors beats paper, you lose!")
        elif rps_input == "scissors":
            if computer == "paper":
                print("Scissors beats paper, you win!")
            if computer == "rock":
                print("Rock beats scissors, you lose!")

        if rps_input not in ["rock", "paper", "scissors"]:
            print("Your input is invalid, please try again")

        #s = "abDSasc"
        #print(s.upper())
        #this is an example on how to convert inputs into lower case and vice versa
main()