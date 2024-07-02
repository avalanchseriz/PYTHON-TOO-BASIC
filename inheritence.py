class Organism:

    alive = True

   

class Animal(Organism):


    def eat(self):
        print("this animal is eating")

    def sleep(sleep):
        print("this animal is sleeping")

class Rabbit(Animal):
    def run():
        print("dun dun dun")
class Fish(Animal):
    def swim():
        print("hehe under the water")
class Hawk(Animal):
    def fly():
        print("nyoooommmmmm!!!!")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
print(hawk.alive)

class Prey:

    def flee(self):
        print("animal fees")

class Predator:

    def hunt(self):
        print("hunting")

class human(Prey, Predator, Animal):
    def pp(self):
        print("i am a human")
