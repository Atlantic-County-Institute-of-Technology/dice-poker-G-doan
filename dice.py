import random


class Dice:
    DEFAULT_ROLL = 1

    def __init__(self):
        self.NUM_FACES = 6
        self.MAX_DICE = 5
        self.dice = []
        self.keep = []

    def roll_dice(self):
        if len(self.dice) != 5:
            for die in range(self.MAX_DICE):
                self.dice.append(random.randint(1, self.NUM_FACES))
                self.keep.append("Roll")
        for die in range(self.MAX_DICE):
            if self.keep[die] != "Keep":
                self.dice[die] = random.randint(1, self.NUM_FACES)
                self.keep[die] = "Roll"
        return self.dice

    def keep_dice(self, die):
        self.keep[die - 1] = "Keep"
        return self.keep



class Die:
    NUM_FACES = 6
    DEFAULT_ROLL = 1

    def __init__(self):
        self.face = self.NUM_FACES
        self.value = self.DEFAULT_ROLL

    def roll(self):
        self.value = random.randint(1, self.NUM_FACES)
        return self.value

    def get_value(self):
        return self.value
