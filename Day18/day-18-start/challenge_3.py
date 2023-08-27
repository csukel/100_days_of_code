from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.width(2)
turtle.colormode(255)


def pick_random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    tim.pencolor(red,green,blue)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    pick_random_color()
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
