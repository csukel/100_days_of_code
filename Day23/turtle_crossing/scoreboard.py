from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
POSITION = (-210, 250)

class Scoreboard(Turtle):
	def __init__(self) -> None:
		super().__init__()
		self.level = 1
		self.penup()
		self.hideturtle()
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(POSITION)
		self.write(f"Level: {self.level}", align=ALIGNMENT,font=FONT)

	def increase_level(self):
		self.level += 1
		self.update_scoreboard()

	def reset(self):
		self.level = 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.write("Game Over.", align=ALIGNMENT,font=FONT)