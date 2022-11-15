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
            print(f"Hero Name: {self.name}") 

    def add_hero(self, hero):
        self.heroes.append(hero)

if __name__ == "__main__":
    spiderman = Team("Spiderman")
    spiderman.add_hero("Spiderman")
    print(spiderman.view_all_heroes())
    batman = Team("Batman")
    batman.add_hero("Spiderman")
    print(batman.view_all_heroes())