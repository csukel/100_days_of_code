import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()

	car_manager.create_cars()
	car_manager.move_cars()

	if car_manager.has_crashed(player):
		game_is_on = False
		scoreboard.game_over()


	if player.has_crossed_finish_line():
		scoreboard.increase_level()
		player.got_to_start()
		car_manager.increse_move_distance()
		car_manager.remove_cars()

screen.exitonclick()
