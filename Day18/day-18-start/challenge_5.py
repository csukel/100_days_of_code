from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.width(1)
turtle.colormode(255)
tim.speed("fastest")


#radius of 100 in distance

def pick_random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return red, green, blue


def draw_spinograph(size_of_gap):
    for degrees in range(0, 361, size_of_gap):
        tim.pencolor(pick_random_color())
        tim.circle(radius=100)
        tim.setheading(degrees)


draw_spinograph(5)

screen = Screen()
screen.exitonclick()
