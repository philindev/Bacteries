from bacterium import BacteriumOne, BacteruimTwo, BacteruimThree, BacteruimFour, BacteruimFive, ImprovedBacterium
import bacterium
from antibiotic import AntibioticStart, AntibioticMedium, AntibioticMaster
import random


class Game:
    def __init__(self):
        self.start = False
        self.finish = False
        self.score = 0
        self.money = 100
        self.time = 0
        self.army = {BacteriumOne: 0, BacteruimTwo: 0, BacteruimThree: 0,
                     BacteruimFour: 0, BacteruimFive: 0, ImprovedBacterium: 0}
        self.wave_count = 0
        self.achieved_waves = set()

    def buy(self, bacteria):
        # self.start = True
        self.money -= bacteria().price
        if self.money <= 0:
            self.money = 0
            return False
        self.army[bacteria] += 1
        return bacteria()

    def killed(self, bacteria, array_bacterias):
        array_bacterias.remove(bacteria)
        self.army[type(bacteria)] -= 1

    def alive(self, bacteria_array):
        if any(bacteria_array):
            self.score += random.randint(2, 50)
            self.money += random.randint(1, 100)

    def wave(self, rest: dict):
        try:
            if any(rest):
                for __ in range(random.randint(0, 5)):
                    for i in range(1, 6):
                        a = random.randint(0, len(rest[i]))
                        if rest[i] and a:
                            try:
                                if len(rest[i]) == 1:
                                    rest[i] = []
                                else:
                                    rest[i].remove(rest[i][a])
                            except IndexError:
                                continue
            count = 0
            for i in range(1, 6):
                count += len(rest[i])
            self.finish = count
            return rest
        except KeyError or IndexError:
            return rest


