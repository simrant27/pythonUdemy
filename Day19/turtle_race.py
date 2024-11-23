import turtle
from random import random
from turtle import Turtle, Screen

import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "blue", "pink", "yellow", "green", "orange"]

y_position = [-70,-40, -10, 20,50,80]
all_turtle =[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -240, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You won! The {winning_turtle} turtle won the race")

            else:
                print(f"You lose! The {winning_turtle} turtle won the race")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

# def create_turtle(color, y):
#     tim = Turtle(shape="turtle")
#     tim.penup()
#     tim.color(color)
#     tim.goto(x= -240,y=y)
#
# pos = -150
# for color in colors:
#     create_turtle(color,pos)
#     pos += 50

screen.exitonclick()