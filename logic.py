from bacterium import BacteriumOne, BacteruimTwo, BacteruimThree, BacteruimFour, BacteruimFive, ImprovedBacterium
import bacterium
from antibiotic import AntibioticStart, AntibioticMedium, AntibioticMaster


class Game:
    def __init__(self):
        self.score = 0
        self.money = 100
        self.time = 0
        self.army = {'BacteriumOne': 0, 'BacteruimTwo': 0, 'BacteruimThree': 0,
                     'BacteruimFour': 0, 'BacteruimFive': 0, 'ImprovedBacterium': 0}
        self.wave_count = 0
        self.achieved_waves = set()

    def wave(self):
        self.wave_count += 1
        self.achieved_waves.add(AntibioticStart())

        if self.wave_count > 5:
            self.achieved_waves.add(AntibioticMedium())
        if self.wave_count > 10:
            self.achieved_waves.add(AntibioticMaster())

        return self.achieved_waves

    def buy(self, bacteria):
        self.money -= bacteria().price
        if self.money <= 0:
            self.money = 0
            return False
        self.army[bacteria] += 1
        return bacteria()

    def killed(self, bacteria, array_bacterias):
        array_bacterias.remove(bacteria)
        self.army[bacteria.__class__.__name__] -= 1

    def alive(self, bacteria_array):
        for bact in bacteria_array:
            for wave in self.achieved_waves:
                self.score += bact.score * wave.bonus
                self.money += bact.cash * wave.bonus

