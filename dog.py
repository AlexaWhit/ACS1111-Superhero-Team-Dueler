class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(f"{self.name} sleeps for hours {self.sleep_duration}")

class Dog(Animal):
    # def __init__(self, name, breed):
    #     self.name = name
    #     self.breed = breed
    #     print("dog initialized!")

    def bark(self):
        print("Woof! Woof!")

    def sit(self):
        print(f"{self.name} sits!")

    def roll_over(self):
        print(f"{self.name} rolls over!")


my_dog = Dog("Freya", 8)
my_dog.sleep()
my_dog.bark()

