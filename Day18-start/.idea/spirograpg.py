import turtle as t
import random

tim = t.Turtle()
s = t.Screen()
s.colormode(255)

tim.speed("fastest")

def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):

    for i in range(0,360, size_of_gap):
        tim.color(get_color())
        tim.circle(100)
        tim.setheading(i)

draw_spirograph(5)


s.exitonclick()