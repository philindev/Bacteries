import pygame, random


CHANGE_COORDS = (-3, -2, -1, 0, 1, 2, 3)


def set_coords():
    return random.randint(0, 895), random.randint(0, 525)


class BaseBacterium:
    def __init__(self, xp, score, time, cash, price, bodyname):
        self.XP = xp
        self.score_bonus = score
        self.cash_bonus = cash
        self.price = price
        self.regeneration_time = time
        self.body = pygame.image.load(bodyname)
        self.sub_available = False
        self.x, self.y = set_coords()

    def __add__(self, other):
        if not other.sub_available:
            return ImprovedBacterium(self.XP + other.XP,
                                     self.score_bonus + self.score_bonus,
                                     self.cash_bonus + other.cash_bonus, 0)

    def __sub__(self, other):
        if other.sub_available:
            self.XP -= other.damage

    def __eq__(self, other):
        return True

    def move(self):
        self.y += random.choice(CHANGE_COORDS)
        self.x += random.choice(CHANGE_COORDS)


class BacteriumOne(BaseBacterium):
    def __init__(self):
        xp = 100
        score = 10
        time = 5
        cash = 40
        price = 30
        bodyname = 'img/creatures/bacteria1.png'
        super().__init__(xp, score, time, cash, price, bodyname)


class BacteruimTwo(BaseBacterium):
    def __init__(self):
        xp = 150
        score = 20
        time = 10
        cash = 80
        price = 60
        bodyname = 'img/creatures/bacteria2.png'
        super().__init__(xp, score, time, cash, price, bodyname)


class BacteruimThree(BaseBacterium):
    def __init__(self):
        xp = 200
        score = 30
        time = 15
        cash = 120
        price = 90
        bodyname = 'img/creatures/bacteria3.png'
        super().__init__(xp, score, time, cash, price, bodyname)


class BacteruimFour(BaseBacterium):
    def __init__(self):
        xp = 250
        score = 40
        time = 20
        cash = 160
        price = 120
        bodyname = 'img/creatures/bacteria4.png'
        super().__init__(xp, score, time, cash, price, bodyname)


class BacteruimFive(BaseBacterium):
    def __init__(self):
        xp = 300
        score = 50
        time = 25
        cash = 200
        price = 150
        bodyname = 'img/creatures/bacteria5.png'
        super().__init__(xp, score, time, cash, price, bodyname)


class ImprovedBacterium(BaseBacterium):
    def __init__(self, *params):
        bodyname = 'img/creatures/bacteria7.png'
        super().__init__(*params, bodyname)
