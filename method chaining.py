import time as t

class Car:

    def turn_on(self):
        print("Engine On")
        return self

    def drive(self):
        print("This is driving")
        return self

    def brake(self):
        print("This has stopped")
        return self

    def turn_off(self):
        print("Engine Off")
        return self

car = Car()

car.turn_on().drive()
t.sleep(1)
car.brake().turn_off()
t.sleep(1)
