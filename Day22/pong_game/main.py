from screen import GameScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGTH = 600

game_screen = GameScreen(screen_width=WIDTH, screen_height=HEIGTH)

paddle_right = Paddle(width=5, height=1, position=(WIDTH // 2 - 50, 0))
paddle_left = Paddle(width=5, height=1, position=(-(WIDTH // 2 - 50), 0))
ball = Ball(width=20, height=20, position=(0, 0), screen_width=WIDTH, screen_height=HEIGTH)
scoreboard = Scoreboard(screen_height=HEIGTH)

game_screen.listen()
game_screen.onkey(paddle_right.go_up, "Up")
game_screen.onkey(paddle_right.go_down, "Down")
game_screen.onkey(paddle_left.go_up, "w")
game_screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
	time.sleep(ball.move_speed)
	game_screen.refresh()
	ball.move()
	ball.detect_collision_with_paddle(paddle_left)
	ball.detect_collision_with_paddle(paddle_right)

	if ball.is_goal():
		if ball.xcor() > 0 :
			#goal for the left paddle
			scoreboard.l_score += 1
		else:
			#goal for the right paddle
			scoreboard.r_score += 1

		scoreboard.update_scoreboard()
		ball.reset_position()


game_screen.exitonclick()
