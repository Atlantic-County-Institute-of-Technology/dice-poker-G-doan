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
from collections import Counter

# Important variables
global dice
dice = Dice()
global straight1
straight1 = [1, 2, 3, 4, 5]
global straight2
straight2 = [2, 3, 4, 5, 6]


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


def game_play():
    # Some Global Variables
    global rolled
    rolled = dice.roll_dice()
    global kept_dice
    kept_dice = []
    # Important variables for the code to run correctly
    rolls = 3
    playing = True
    while playing:
        if rolls == 1:
            playing = False
        os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
        print(f"Rolls Remaining: {rolls}")  # Print for the number of rolls left
        print(f"Your Roll: {rolled}")  # Print to show dice roll
        score = get_score(rolled)  # Calls on function to get the value of the hand
        hand_type = hand_evaluate(score)  # Calls on function to get the type of hand
        print(f"You got {hand_type}\n")  # Print for the type of hand you have
        # Inquirer menu for the actual game
        questions = [
            inquirer3.List('menu',
                           message="Select action",

                           choices=['Roll Dice', 'Keep Dice'])
        ]
        answers = inquirer3.prompt(questions)
        select = "{}".format(answers['menu'])
        # Code for what the user selects
        match select:
            # If user chooses to roll the dice again
            case "Roll Dice":
                rolls -= 1
                os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
                rolled = dice.roll_dice()
                print(f"Your Roll: {rolled}\n")  # Print to show dice roll
            case "Keep Dice":
                os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
                print(f"Your Roll: {rolled}\n")  # Print to show dice roll
                kept_dice = keep_select(kept_dice)  # Code to get call on select kept dice function
                # Code to keep the dice in dice class
                for i in range(len(kept_dice)):
                    dice.keep_dice(int(kept_dice[i]))
    os.system('cls' if os.name == 'nt' else 'clear')  # Code to clear old text
    print(f"Final Hand: {rolled}")
    score = get_score(rolled)  # Calls on function to get the value of the hand
    hand_type = hand_evaluate(score)
    print(f"You got {hand_type}\n")


# Function to ge the point worth of your hand
def get_score(hand):
    sorted_hand = sorted(hand)
    counts = Counter(hand)
    hand_value = sorted(counts.values(), reverse=True)  # To get how many times a number appears
    unique_values = sorted(counts.keys(), reverse=True)  # To get the value of the unique die
    straight = straight_check(sorted_hand)  # Calls on the function for checking for a straight
    if hand_value[0] == 5:
        score_value = 7
    elif hand_value[0] == 4:
        score_value = 6
    elif hand_value == [3, 2]:
        score_value = 5
    elif hand_value[0] == 3:
        score_value = 3
    elif hand_value == [2, 2, 1]:
        score_value = 2
    elif hand_value[0] == 2:
        score_value = 1
    elif hand_value[0] == 1:
        if straight == "yes":
            score_value = 4
        else:
            score_value = 0
    return score_value


# Function to get the type of hand
def hand_evaluate(hand_score):
    hand_types = ["Bust", "2 of a kind", "2 Pairs", "3 of a kind",
                  "Straight", "Full House", "4 of a kind", "5 of a kind"]
    return hand_types[hand_score]


# Function that checks if the hand is a straight
def straight_check(check):
    global straight1, straight2
    if check == straight1:
        straight = "yes"
        return straight
    elif check == straight2:
        straight = "yes"
        return straight
    else:
        straight = "no"
        return straight


# The main function used
def main():
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
                game_play()  # Calls on the function that actually plays the game

            case "Exit":
                exit()


if __name__ == '__main__':
    main()
