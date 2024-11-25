from turtle import Screen
from food import Food
import time

from scoreboard import Score
from snake import Snake


screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        game_is_on = False
        score.game_over()


    #detect collsion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()


screen.exitonclick()