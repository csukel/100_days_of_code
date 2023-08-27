from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
DATA_FILE_PATH = "/Users/l.stylianou/Development/python/100-days-of-code/Day20/snake_game/data.txt"
class Scoreboard(Turtle):
	def __init__(self, canvas_height):
		super().__init__()
		self.score = 0
		self.read_high_score()
		self.goto(0, canvas_height// 2 - 40)
		self.pencolor("white")
		self.update_scoreboard()
		self.hideturtle()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)

	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.write(f"Game over.", align=ALIGNMENT,font=FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			self.write_high_score(self.score)
		self.score = 0
		self.update_scoreboard()

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def read_high_score(self):
		with open(DATA_FILE_PATH) as file:
			self.high_score = int(file.read())

	def write_high_score(self, score):
		with open(DATA_FILE_PATH, "w") as file:
			file.write(str(score))
