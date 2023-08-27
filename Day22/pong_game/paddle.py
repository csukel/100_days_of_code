from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, width, height, position) -> None:
		super().__init__(shape="square")
		self.color("white")
		self.shapesize(stretch_wid=width, stretch_len=height)
		self.penup()
		self.goto(position)

	def go_up(self):
		self.goto(self.xcor(), self.ycor() + 20)

	def go_down(self):
		self.goto(self.xcor(), self.ycor() - 20)


