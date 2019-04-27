import pygame, index
from bacterium import BacteriumOne, BacteruimTwo, BacteruimThree, BacteruimFour, BacteruimFive, ImprovedBacterium


class Game:
    def __init__(self):
        self.score = 0
        self.money = 100
        self.time = 0
        self.army = {BacteriumOne: 0, BacteruimTwo:0, BacteruimThree: 0,
                     BacteruimFour: 0, BacteruimFive: 0, ImprovedBacterium: 0}

