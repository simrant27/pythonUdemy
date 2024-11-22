import random
from turtle import Turtle, Screen

# from coffeeMachine.main import choice

tim = Turtle()
colors = ["Blue", "Green", "LightGoldenrodYellow", "Red", "Pink"]
s = Screen()
# # angle = 360 / i
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
#
for i in range(3,10):
    tim.color(random.choice(colors))
    angle = 360 / i
    for j in range(i):
        tim.forward(100)

        tim.right(angle)


s.exitonclick()