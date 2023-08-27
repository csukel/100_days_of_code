from turtle import Turtle
from typing import List

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


	def __init__(self, no_of_segments) -> None:
		self.snake_body: List[Turtle] = []
		self.create_snake(no_of_segments)
		self.head = self.snake_body[0]


	def create_snake(self, no_of_segments):
		for i in range(no_of_segments):
			self.add_square((i*-20, 0))


	def move(self):
		# for i in reversed(range(len(self.snake_body))):
		for i in reversed(range(1, len(self.snake_body))):
			self.snake_body[i].goto(self.snake_body[i-1].pos())
		self.head.forward(MOVE_DISTANCE)

	def add_square(self, position) -> Turtle:
		square = Turtle(shape="square")
		square.penup()
		square.color("white")
		square.goto(position)
		self.snake_body.append(square)

	def grow(self):
		self.add_square(self.snake_body[-1].position())


	def detect_collision_with_tail(self):
		"""check if the snake's head collided to its body"""
		for i in range(1, len(self.snake_body)):
			if self.head.distance(self.snake_body[i].pos()) < 1:
				return True

		return False

	def detect_collision_with_wall(self, canvas_width, canvas_height) -> bool:
		"""detect snake collisions with the surrounding walls"""
		wall_ycor = canvas_height / 2
		wall_xcor = canvas_width / 2

		head_xcor = self.head.xcor()
		head_ycor = self.head.ycor()

		if abs(head_xcor) > wall_xcor or abs(head_ycor) > wall_ycor:
			return True

		return False

	def detect_collision_with_food(self, food: Turtle):
		"""detect collision with food"""
		# print(f"Snake pos: {self.head.pos()} / Food pos: {food.pos()} / Distance {self.head.distance(food.pos())} / Equal? : {self.head.distance(food.pos()) == 0}")
		if self.head.distance(food.pos()) < 15:
			return True
		
		return False

	def set_heading(self, degrees: float):
		self.head.setheading(degrees)


	def arrow_up(self):
		if self.head.heading() != DOWN:
			self.set_heading(UP)


	def arrow_left(self):
		if self.head.heading() != RIGHT:
			self.set_heading(LEFT)


	def arrow_right(self):
		if self.head.heading() != LEFT:
			self.set_heading(RIGHT)


	def arrow_down(self):
		if self.head.heading() != UP:
			self.set_heading(DOWN)

	def reset(self):
		for square in self.snake_body:
			square.goto(1000 , 1000)
		self.snake_body.clear()
		self.create_snake(3)
		self.head = self.snake_body[0]

