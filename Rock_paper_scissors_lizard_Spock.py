#coding=utf8
# Rock-paper-scissors-lizard-Spock template
# import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random


def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # pass
    number = -1;
    # convert name to number using if/elif/else
    if name == "rock":
    	number = 0
    elif name == "Spock":
    	number = 1
    elif name == "paper":
    	number = 2
    elif name == "lizard":
    	number = 3
    else:
    	number = 4
    # don't forget to return the result!
    return number

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # pass
    
    # convert number to a name using if/elif/else
    name = ""
    if number == 0:
    	name ="rock"
    elif number ==1:
    	name = "Spock"
    elif number == 2:
    	name = "paper"
    elif number == 3:
    	name = "lizard"
    else:
    	name = "scissors"
    # don't forget to return the result!
    return name
    

def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    # pass
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    modulo = comp_number - player_number
    # use if/elif/else to determine winner, print winner message
    if modulo > 0:
        print "Computer wins!"
    elif modulo == 0:
        print "Player and computer tie!"
    else:
        print "Player wins!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


# Test calls to number_to_name()
# print number_to_name(0)
# print number_to_name(1)
# print number_to_name(2)
# print number_to_name(3)
# print number_to_name(4)

# Test calls to name_to_number()
# print name_to_number("rock")
# print name_to_number("Spock")
# print name_to_number("paper")
# print name_to_number("lizard")
# print name_to_number("scissors")