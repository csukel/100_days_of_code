from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):
	def __init__(self) -> None:
		super().__init__(shape="turtle")
		self.setheading(HEADING)
		self.penup()
		self.got_to_start()


	def move(self):
		self.forward(MOVE_DISTANCE)

	def has_crossed_finish_line(self):
		if self.ycor() > FINISH_LINE_Y:
			return True
		
		return False
	
	def got_to_start(self):
		self.goto(STARTING_POSITION)
