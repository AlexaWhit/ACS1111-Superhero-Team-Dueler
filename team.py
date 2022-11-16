import random
from ability import Ability
from hero import Hero


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    # Remove a hero from the team
    def remove_hero(self, name):
        foundHero = False
        #loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set indicator to True
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(f"Hero Name: {hero.name}") 

    def add_hero(self, hero):
        self.heroes.append(hero)

    # Print team statistics
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    # Reset all heroes health to starting_health
    def revive_heroes(self, starting_health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} has been revived and health has increased!")
           

    # Battle each team against each other
    def attack(self, other_team):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Randomly select a living hero from each team
            hero1 = random.choice(living_heroes) 
            hero2 = random.choice(living_opponents)
            # Have the heroes fight each other
            hero1.fight(hero2)
            # Update active roster based on who dies
            if hero1.is_alive() == False:
                living_heroes.remove(hero1)
            elif hero2.is_alive() == False:
                living_opponents.remove(hero2)


    

# if __name__ == "__main__":
#     spiderman = Team("Spiderman")
#     spiderman.add_hero("Spiderman")
#     print(spiderman.view_all_heroes())
#     batman = Team("Batman")
#     batman.add_hero("Spiderman")
#     print(batman.view_all_heroes())