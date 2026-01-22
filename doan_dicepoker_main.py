# Creator: Gavin Doan
# Objective
# Date Made: 1/13/26
# Last Edited: 1/14/26


# Hands of Dice Poker
# 5 of a Kind
# 4 of a kind
# Full house(3 of a kind + 2 of a kind)
# Straight(1 of each value)
# 3 of a kind
# Two Pairs
# Two of a kind


# Imports
import inquirer3
import os
from dice import Dice
from sort_hand import

# Important variables
global dice
dice = Dice()


# Function to Select dice to keep
def keep_select(kept_list):
    # Inquirer checkbox menu for user to select dice to keep
    questions = [
        inquirer3.Checkbox(
            'Keep',
            message="Select Dice to keep",
            choices=[
                ('Dice 1', '1'),
                ('Dice 2', '2'),
                ('Dice 3', '3'),
                ('Dice 4', '4'),
                ('Dice 5', '5')],
            # Sets the default kept to previously selected kept dice
            default=[f"{kept_list[die]}" for die in range(len(kept_list))] if len(kept_list) != 0 else None),
            ]
    answers = inquirer3.prompt(questions)
    keep_dice = answers["Keep"]  # set to variable for easy use
    # To set dice as a kept in the class
    for i in range(len(keep_dice)):  # To add kept dice to kept_list
        if keep_dice[i] not in kept_list:  # To prevent adding repeats to kept_list
            kept_list.append(int(keep_dice[i]))  # Adds selected dice into list if was newly added
    return kept_list


def get_score(hand):
    if '1' in hand:

    # kind5 = 7
    # kind4 = 6
    # full = 5
    # straight = 4
    # kind3 = 3
    # pair2 = 2
    # kind2 = 1
    # empty = 0

def main():
    # global variables
    global kept_dice
    kept_dice = []
    # To give initial rolled dice and show user values
    while True:
        # Inquirer menu to start the Game
        questions = [
            inquirer3.List('menu',
                           message="What would you like to do?",

                           choices=['Start Game', 'Exit'])
        ]
        answers = inquirer3.prompt(questions)
        select = "{}".format(answers['menu'])
        # Match select for the start menu
        match select:
            case "Start Game":
                # global variable for dice roll
                global rolled
                rolled = dice.roll_dice()
                print(f"Your Roll: {rolled}\n")  # Print to show dice roll
                get_score(rolled)
                # while loop for the actual game
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
                    print(f"Your Roll: {rolled}\n")  # Print to show dice roll
                    # print(f"score:{score}")  # Print for the score
                    get_score(rolled)
                    # Inquirer menu for the actual game
                    questions = [
                        inquirer3.List('menu',
                                       message="Select dice to keep",

                                       choices=['Roll Dice', 'Keep Dice'])
                    ]
                    answers = inquirer3.prompt(questions)
                    select = "{}".format(answers['menu'])
                    # Code for what the user selects
                    match select:
                        # If user chooses to roll the dice again
                        case "Roll Dice":
                            os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
                            rolled = dice.roll_dice()
                            print(f"Your Roll: {rolled}\n")  # Print to show dice roll
                            get_score(rolled)
                        case "Keep Dice":
                            os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
                            print(f"Your Roll: {rolled}\n")  # Print to show dice roll
                            kept_dice = keep_select(kept_dice)  # Code to get call on select kept dice function
                            # Code to keep the dice in dice class
                            for i in range(len(kept_dice)):
                                dice.keep_dice(int(kept_dice[i]))
            case "Exit":
                exit()


if __name__ == '__main__':
    main()

