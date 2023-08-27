from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.width(10)
turtle.colormode(255)
tim.speed("fastest")

STEPS = 50
DEGREES = 90
directions = [0, 90, 180, 270]


def change_direction_randomly():
    for _ in range(random.randint(1,4)):
        tim.setheading(random.choice(directions))


def pick_random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return red, green, blue


for _ in range(100):
    tim.pencolor(pick_random_color())
    tim.forward(STEPS)
    change_direction_randomly()

screen = Screen()
screen.exitonclick()
