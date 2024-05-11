from os import access
from random import choice
import numpy as np
import scoreSheet as scoreSheet

def newGame():
    # Rounds in the game of Yahtzee = 13
    # Max number of players is 10 
    test = "test"

def showRules():
    rules = '''********************************************************************************
*** 1.   Roll 5 dice to score combinations, to reach a combined high score!  ***
*** 2.  Each turn you will roll 5 dice, up to 3 times to score a comination  ***
*** 3. After 3 roles you must place a score, or a 0, in one of 13 categories ***
********************************************************************************
'''
    print(rules)

def roll():
    #function to roll dice that aren't on hold
    test = "Test"

def main():
    
    '''
    Play order is determined by one roll of all 5 by all players. 
    Highest total first, then pass to the left 
    Rules:
    Each turn (13) roll the die up to 3 times
    At the end place a score of a 0 in one of the 13 categories 

    Turn: 3 of [Roll, Mark Keepers, Stop and set a score]
    
    '''
    welcome = "Let's play Yahtzee!"
    directions = "If you need to know the rules, type 1 and press Enter. \nIf you would like to start a new game, type 2 and press Enter\n"

    print(welcome)
    choice = input(directions)

    match choice:
        case "1":
            showRules()
            main()
        case "2":
            newGame()
        case _:
            print("I'm sorry, I didn't understand. Let me return you to the main menu")
            main()

if __name__ == "__main__":
    main()