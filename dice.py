import random

class Dice:
    def __init__(self, sides=6, num_dice=1):
        self.sides = sides
        self.num_dice = num_dice

    def roll(self):
        return sum(random.randint(1, self.sides) for _ in range(self.num_dice))
