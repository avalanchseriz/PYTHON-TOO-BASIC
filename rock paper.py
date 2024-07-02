import random as r
import time as t

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = r.choice(choices)
    player = None

    while player not in choices:
     player = input("rock, paper or scissors?: ")

    if player == computer:
        print("computer: ", computer)
        t.sleep(1)
        print("player: ",player)
        t.sleep(1)
        print("Tie!!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you lose!!")
        if computer == "scissors":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you win!!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you lose!!")
        if computer == "rock":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you win!!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you lose!!")
        if computer == "paper":
            print("computer: ", computer)
            t.sleep(1)
            print("player: ",player)
            t.sleep(1)
            print("you win!!")

    play_again = input("play again (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")