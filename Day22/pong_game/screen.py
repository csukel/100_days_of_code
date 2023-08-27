from turtle import Screen

class GameScreen():
	def __init__(self, screen_width, screen_height):
		self._screen = Screen()
		self.screen.setup(width=screen_width, height=screen_height)
		self.screen.bgcolor("black")
		self.screen.title("Pong Game")
		self.screen.tracer(0) #turn tracer off

	@property
	def screen(self):
		return self._screen

	def refresh(self):
		self.screen.update()

	def exitonclick(self):
		self.screen.exitonclick()

	def listen(self):
		self.screen.listen()

	def onkey(self, fun, key):
		self.screen.onkey(fun , key)
