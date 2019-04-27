import pygame, random


def set_center():
    return random.randint(0, 775), random.randint(0, 515)


class BaseAntibiotic:
    def __init__(self, damage, coofic, epicenter):
        self.damage = damage
        self.bonus = coofic
        self.center = set_center()
        self.radius = 30
        self.count_to_upgrade = 0
        self.lesion_area = epicenter
        self.sub_available = True


class AntibioticStart(BaseAntibiotic):
    def __init__(self):
        damage = 70
        bonus = 2
        epicenter = 100
        super().__init__(damage, bonus, epicenter)


class AntibioticMedium(BaseAntibiotic):
    def __init__(self):
        damage = 100
        bonus = 3
        epicenter = 150
        super().__init__(damage, bonus, epicenter)


class AntibioticMaster(BaseAntibiotic):
    def __init__(self):
        damage = 130
        bonus = 4
        epicenter = 200
        super().__init__(damage, bonus, epicenter)


