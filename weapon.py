import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        weapon_damage = random.randint(self.max_damage // 2, self.max_damage)
        return weapon_damage

