from turtle import Turtle
import random
from typing import List

class Food(Turtle):
	def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True, canvas_width: int = 300, canvas_height: int = 300, size: float = 0.5) -> None:
		super().__init__(shape, undobuffersize, visible)
		super().color('blue')
		super().shapesize(size, size)
		self.penup()
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height

	
	def get_random_pos(self):
		c_width = self.canvas_width // 2
		c_height = self.canvas_height // 2

		xcor = random.randrange(0, c_width, 20) * random.choice([1,-1])
		ycor = random.randrange(0, c_height, 20) * random.choice([1,-1])

		return (xcor, ycor)
	
	def set_random_pos(self, snake_body: List[Turtle]):
		snake_pos = []
		for snake_part in snake_body:
			snake_pos.append(snake_part.pos())
		
		while True:
			new_pos = self.get_random_pos()
			if new_pos not in snake_pos:
				self.goto(new_pos)
				break