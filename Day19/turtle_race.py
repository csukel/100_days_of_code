import random
import turtle
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tutles = []
WIDTH = 500
HEIGHT = 400

screen = Screen()
turtle.speed("fastest")
screen.setup(width=WIDTH, height=HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

def get_set():
    y = -130
    screen.clear()
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(-230, y)
        tutles.append(turtle)
        y += 50



def go():
    is_race_on = True
    winner = ""
    while is_race_on:
        turtle = random.choice(tutles)
        turtle.forward(random.randint(0, 10))
        current_x_pos = turtle.pos()[0]
        if current_x_pos > (WIDTH / 2) - 20:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"Winner is {winner} turtle!!")

    if winner == user_bet:
        print(f"You've won! The {winner} turtle is the winner!")
    else:
        print(f"You've lost! The {winner} turtle is the winner!")



get_set()

go()

screen.exitonclick()