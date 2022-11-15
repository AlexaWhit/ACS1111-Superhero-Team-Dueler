from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the numerical max damage of the ability?  ")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?  ")
        weapon_damage = input("What is the numerical damage of the weapon?  ")
        return Weapon(name, weapon_damage)

    def create_armor(self):
        name = input("What is the armor name?  ")
        max_block= input("What is the numerical max blockage of the weapon?  ")
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        running = True
        while running == True:
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
            elif add_item == "4":
                running = False
        return hero

    def build_team_one(self):
        num_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        num_team_members = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    # Battle Team One and Team Two together
    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats_team(self):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team.name + " average K/D was: " + str(team_kills/team_deaths))

    def show_survivors(self, team):
        survivors = 0
        for hero in team.heroes:
            if hero.deaths == 0:
                survivors += 1
                print("\n"f"{hero.name} from {team.name} survived the battle!")
        return survivors
    

    def show_stats(self):
        team_one_survivors = self.survivors(self.team_one)
        team_two_survivors = self.survivors(self.team_two)

        if team_one_survivors > team_two_survivors:
            print(f"Team One wins the battle!")
        else:
            print(f"Team Two wins the battle!")

        
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")


    def team_two_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()



    
