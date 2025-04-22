import turtle
import random

for i in range(100):
    length = random.randrange(100)
    heading = random.randrange(360)
    turtle.setheading(heading)
    turtle.forward(length)
