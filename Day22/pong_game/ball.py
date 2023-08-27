from turtle import Turtle
from screen import GameScreen

class Ball(Turtle):
	def __init__(self, width, height , position, screen_height, screen_width) -> None:
		super().__init__(shape="circle")
		self.color("white")
		self.penup()
		self.goto(position)
		self.setheading(45)
		self._screen_width = screen_width
		self._screen_height = screen_height
		self._move_x = 10
		self._move_y = 10
		self.move_speed = 0.1


	def move(self):
		self.goto(self.xcor() + self._move_x , self.ycor() + self._move_y)
		self.detect_collision_with_wall()


	def bounce_y(self):
		self._move_y *= -1


	def bounce_x(self):
		self._move_x *= -1
		self.move_speed *= 0.9


	def detect_collision_with_wall(self):
		"""This method detects collision with upper and lower wall (y-axis) and
			give the ball a bouncing movement (change heading accordingly)
			We don't care about the left and right wall as those are used to 
			count the score
		"""
		top_y = self._screen_height // 2
		bottom_y = self._screen_height // 2 * -1

		if self.ycor() > top_y - 20 or self.ycor() < bottom_y + 20:
			#collision with top wall
			self.bounce_y()


	def detect_collision_with_paddle(self, paddle: Turtle):
		# print(f"Distance {self.distance(paddle.pos())}")
		if self.distance(paddle.pos()) < 50 and abs(self.xcor()) > 320:
			self.bounce_x()

	def is_goal(self):
		if (abs(self.xcor()) > self._screen_width // 2 - 10):
			return True
		
		return False


	def reset_position(self):
		self.goto(0, 0)
		self.bounce_x()
		self.move_speed = 0.1
