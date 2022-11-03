from operator import truediv
import random
from timeit import repeat
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

    def random_fight(self, opponent):
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
        fight = True 
        hero2 = opponent
        if hero1.abilities and hero2.abilities == 0:
            print("DRAW!")
        # Start Fight!
        else:
            while fight is True:
                if hero1.is_alive() is False:
                    print (f"{hero2.name} won!")
                    break
                elif hero2.is_alive() is False:
                    print (f"{hero1.name} won!")
                    break
                else:
                    hero1.add_ability()
                    hero2.add_ability()
                    hero1.attack()
                    hero2.defend()
                    hero2.take_damage()
                    hero1.take_damage()
                    hero2.is_alive()
                    if hero2.is_alive is False:
                        print (f"{hero1.name} won!")
                        break
                    hero1.is_alive()
                    if hero1.is_alive() is False:
                        print (f"{hero2.name} won!")
                        break
                    hero2.attack()
                    hero1.defend()
                    hero1.take_damage()
                    hero2.take_damage()
                    repeat


  # 1) else, start the fighting loop until a hero has won
  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop





if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # hero1.fight(hero2)