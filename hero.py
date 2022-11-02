import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        opponent = hero2
        winner = random.randint(0,1)        
        #Stretch Goal: fancy message
        if winner == 1:
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}!")



if __name__ == "__main__":
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)