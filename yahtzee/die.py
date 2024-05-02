import random

def __init__(self, sides=6):
    self.roll_history = []
    self.sides = sides

def roll(self):
    value = random.randint(1,6)
    self.roll_history.append(value)
    return value