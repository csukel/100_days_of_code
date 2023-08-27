from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn tracer off

snake = Snake(3)
food = Food(canvas_width=WIDTH, canvas_height=HEIGHT)
food.set_random_pos(snake.snake_body)
scoreboard = Scoreboard(canvas_height=HEIGHT)

def pause():
	time.sleep(10)
	
def run():
	game_is_on = True
	while game_is_on:
		screen.update()
		time.sleep(0.1)
		snake.move()

		if snake.detect_collision_with_food(food):
			food.set_random_pos(snake.snake_body)
			scoreboard.increase_score()
			snake.grow()

		if snake.detect_collision_with_wall(canvas_width=WIDTH, canvas_height=HEIGHT) or snake.detect_collision_with_tail():
			scoreboard.reset()
			snake.reset()


screen.listen()
screen.onkey(fun=snake.arrow_up, key="Up")
screen.onkey(fun=snake.arrow_left, key="Left")
screen.onkey(fun=snake.arrow_right, key="Right")
screen.onkey(fun=snake.arrow_down, key="Down")

screen.onkey(fun=pause,key="space")


run()

screen.exitonclick()
