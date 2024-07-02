class Car:

    color = None

class Bike():
    color = None




def change_color(car,color):
    car.color = color


car1 = Car()
car2 = Car()
car3 = Car()

bike_1 = Bike()


change_color(car1, "red")
change_color(car2, "white")
change_color(car3, "blue")
change_color(bike_1, "black")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike_1.color)

