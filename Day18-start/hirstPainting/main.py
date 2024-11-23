from random import random

import colorgram
import turtle as t
import random


tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.goto(-200,-200)
tim.hideturtle()

# tim.goto(-50,-50)
s = t.Screen()
s.colormode(255)
rgb_colors = []
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
               (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
# print(rgb_colors)

def generate_in_row():
    for i in range(10):
        # tim.pendown()
        # tim.color(random.choice(color_list))
        # tim.begin_fill()
        # tim.circle(10)
        # tim.end_fill()
        tim.dot(20, random.choice(color_list))
        # tim.penup()
        tim.forward(50)

for i in range(10):
    generate_in_row()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)

    tim.right(180)

s.exitonclick()