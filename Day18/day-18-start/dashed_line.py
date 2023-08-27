from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pencolor("brown")
tim.width(3)

for i in range(10):
   tim.forward(15)
   tim.up()
   tim.forward(15)
   tim.down()

screen = Screen()
screen.exitonclick()
