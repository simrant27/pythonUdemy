import turtle as t

import random

from numpy.lib.function_base import angle

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [90,270,180,0]
tim.pensize(10)
tim.speed("fastest")

dist = 0

for _ in range(200):

    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

screen.exitonclick()