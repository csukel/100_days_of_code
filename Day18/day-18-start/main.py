from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pencolor("brown")


def draw_square(x):
    """Function is used to move the turtle into a shape of square"""
    for i in range(4):
        tim.forward(x)
        tim.right(90) #turn right by 90 degrees


draw_square(100)

screen = Screen()
screen.exitonclick()
