import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        # Abilities and armos don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        winner = random.randint(0,1)        
        #Stretch Goal: fancy message
        if winner == 1:
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}!")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        # loop through hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    # TODO: Make sure to take into account that there may not be any armor objects in the list. 
    # Or that if a hero is dead (has no health) they should have 0 defense.
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    # TODO
    def take_damage(self, damage):
        damage_done = damage - self.defend()
        self.current_health -= damage_done
        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent): # Fight each hero until a victor emerges.
        if self.abilities == 0:
            print("DRAW!")
        else:
            while 
  # 1) else, start the fighting loop until a hero has won
  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop






if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # hero1.fight(hero2)