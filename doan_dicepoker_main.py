# Creator: Gavin Doan
# Objective
# Date Made: 1/13/26
# Last Edited: 1/14/26


# Imports
import inquirer3
from dice import Dice

global dice
dice = Dice()
# print(dice.roll_dice())
# print(dice.roll_dice()[4])
# print(dice.keep_dice(5))

def keep_select():
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
                ('Dice 5', '5')]),
            # default=[f"something soon"]),
        ]
    answers = inquirer3.prompt(questions)
    keep_dice = answers["Keep"]  # set to variable for easy use
    # To set dice as a kept in the class
    for i in range(len(keep_dice)):
        dice.keep_dice(int(keep_dice[i]))


def main():
    while True:
        questions = [
            inquirer3.List('menu',
                           message="What would you like to do?",

                           choices=['Start Game', 'Exit'])
        ]
        answers = inquirer3.prompt(questions)
        select = "{}".format(answers['menu'])

        match select:
            case "Start Game":
                rolled = dice.roll_dice()
                print(rolled)
                while True:
                    questions = [
                        inquirer3.List('menu',
                                       message="Select dice to keep",

                                       choices=['Roll Dice', 'Keep Dice'])
                    ]
                    answers = inquirer3.prompt(questions)
                    select = "{}".format(answers['menu'])

                    match select:
                        case "Roll Dice":
                            rolled = dice.roll_dice()
                        case "Keep Dice":
                            keep_select()

            case "Exit":
                exit()








if __name__ == '__main__':
    main()

