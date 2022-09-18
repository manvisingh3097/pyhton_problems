from random import random

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

# print(name_to_number("rock"))
# print(name_to_number("spock"))
# print(name_to_number("paper"))
# print(name_to_number("lizard"))
# print(name_to_number("scissors"))

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"


def rspls(player_choice):
    print("")
    print("user picked :",player_choice )
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    print("comp picked :" , number_to_name(comp_number))
    result = (comp_number - player_number) % 5 
    if result == 1 or result == 2:
        print("computer wins")
    elif result == 0:
        print("draw")
    else :
        print("player wins")

rspls("spock")
