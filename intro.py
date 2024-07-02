import turtle
import math
bob = turtle.Turtle()
sigma = turtle.Turtle()
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)
sigma.penup()
sigma.left(90)
sigma.forward(200)
sigma.left(90)
sigma.forward(200)
sigma.left(60)
sigma.pendown()

sigma.forward(80)
sigma.right(180)
sigma.forward(80)
sigma.right(120)
sigma.forward(80)

bob.color("red","yellow")
bob.speed(10)

bob.begin_fill()
for i in range(2000):
    bob.forward(math.sin(i/10)*25)
    bob.left(20)
bob.end_fill()



turtle.done()