from turtle import Turtle
import random
from typing import List
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
	def __init__(self) -> None:
		self.all_cars : List( Turtle ) = []
		self.move_distance = STARTING_MOVE_DISTANCE
				
	def create_cars(self):
		random_chance = random.randint(1, 6)
		if random_chance == 1:
			new_car = Turtle("square")
			new_car.shapesize(stretch_wid=1, stretch_len=2)
			new_car.color(random.choice(COLORS))
			new_car.penup()
			random_y = random.randint(-250, 250)
			new_car.goto(300, random_y)
			new_car.setheading(180)
			self.all_cars.append(new_car)

	def move_cars(self):
		for car in self.all_cars:
			car.forward(self.move_distance)

	def increse_move_distance(self):
		self.move_distance += MOVE_INCREMENT

	def reset(self):
		self.all_cars : List( Turtle ) = []
		self.move_distance = STARTING_MOVE_DISTANCE

	def has_crashed(self, player):
		for car in self.all_cars:
			if player.distance(car.pos()) < 25:
				return True
			
		return False
	
	def remove_cars(self):
		for car in self.all_cars:
			if abs(car.xcor()) > 300:
				self.all_cars.remove(car)