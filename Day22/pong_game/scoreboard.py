from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):
	def __init__(self, screen_height):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self._screen_height = screen_height
		self.update_scoreboard()


	def update_scoreboard(self):
		self.clear()
		self.goto(-100, self._screen_height // 2 - 100)
		self.write(f"{self.l_score}", align=ALIGNMENT,font=FONT)
		self.goto(100, self._screen_height // 2 - 100)
		self.write(f"{self.r_score}", align=ALIGNMENT,font=FONT)