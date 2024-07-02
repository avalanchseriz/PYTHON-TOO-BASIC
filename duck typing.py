class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is qualking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this cicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)

