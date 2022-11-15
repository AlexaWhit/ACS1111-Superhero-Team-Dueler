class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")

cat = Animal("Freya")
new_frog = Frog("Jumpers")

cat.eat()
cat.drink()
new_frog.eat()
new_frog.drink()
new_frog.jump()