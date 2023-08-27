from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
STEP = 20
DEGREE_STEP = 10

def move_forwards():
    tim.forward(STEP)


def move_backwrods():
    tim.backward(STEP)


def head_counter_clockwise():
    tim.setheading(tim.heading() + DEGREE_STEP)


def head_clockwise():
    tim.setheading(tim.heading() - DEGREE_STEP)


def reset():
    tim.home()
    tim.setheading(0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwrods)
screen.onkey(key="a", fun=head_counter_clockwise)
screen.onkey(key="d", fun=head_clockwise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()