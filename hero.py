from operator import truediv
import random
from timeit import repeat
from ability import Ability 
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        # Abilities and armos don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        # Add deaths and kills which default start at 0
        self.deaths = 0
        self.kills = 0

    # def random_fight(self, opponent):
    #     winner = random.randint(0,1)        
    #     #Stretch Goal: fancy message
    #     if winner == 1:
    #         print(f"{self.name} defeats {opponent.name}!")
    #     else:
    #         print(f"{opponent.name} defeats {self.name}!")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        # loop through hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += int(ability.attack())
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    # Add Weapons
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    # Add Kill
    def add_kill(self, num_kills):
        # update self.kills by num_kills amount
        self.kills += num_kills

    # Add Death
    def add_death(self, num_deaths):
        # update self.deaths by num_deaths amount
        self.deaths += num_deaths

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        damage_done = damage - self.defend()
        self.current_health -= damage_done
        if self.current_health > 0:
            print(f"{self.name} took {damage_done} damage and has {self.current_health} health remaining!")
        elif self.current_health <= 0:
            print(f"{self.name} took {damage_done} damage and has died in the battle!")
        return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    # Fight each hero until a victor emerges.
    def fight(self, opponent): 
        fight = True 
        while fight == True:
            damage_done = self.attack()
            opponent_damage_done = int(opponent.attack())
            self.take_damage(opponent_damage_done)
            opponent.take_damage(damage_done)

             # Check to see if at least one hero has abilities. If no hero has abilities, print "Draw"
            if self.abilities and opponent.abilities == 0:
                print("DRAW!")
            # Start Fight!
            else:
                # Opponent defeats hero
                if self.is_alive() == False and opponent.is_alive() == True:
                    print (f"{opponent.name} won!")
                    self.add_death(1)
                    opponent.add_kill(1)
                    break
                # Hero defeats opponent
                elif self.is_alive() == True and opponent.is_alive() == False:
                    print (f"{self.name} won!")
                    opponent.add_death(1)
                    self.add_kill(1)
                    break
                # Both die
                elif self.is_alive() == False and opponent.is_alive() == False:
                    print (f"Both heroes have died!")
                    opponent.add_death(1)
                    opponent.add_kill(1)
                    self.add_death(1)
                    self.add_kill(1)
                    break

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # hero1.fight(hero2)