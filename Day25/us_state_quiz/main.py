import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/l.stylianou/Development/udemy/100-days-of-code/Day25/us_state_quiz/blank_states_img.gif"
screen.addshape(image)
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

turtle.shape(image)

states_data = pandas.read_csv("/Users/l.stylianou/Development/udemy/100-days-of-code/Day25/us_state_quiz/50_states.csv")
no_correct_states = 0

states = states_data.state.to_list()
print(states)

game_is_on = True
while game_is_on:
	state_name = turtle.textinput(f"{no_correct_states}/50 States Correct" ,"What's another state name?")
	if state_name is None or state_name.title() == 'Exit':
		game_is_on = False
		missing_data = pandas.DataFrame(states)
		missing_data.to_csv("/Users/l.stylianou/Development/udemy/100-days-of-code/Day25/us_state_quiz/states_to_learn.csv")
	else:
		state_name = state_name.title()
		if state_name in states:
			row = states_data[states_data.state == state_name]
			coordinates = (float(row.x), float(row.y))
			state_mark = turtle.Turtle()
			state_mark.penup()
			state_mark.hideturtle()
			state_mark.goto(coordinates)
			state_mark.write(f"{state_name}", align=ALIGNMENT,font=FONT)
			no_correct_states += 1
			states.remove(state_name)
		
		if no_correct_states == 50:
			game_is_on = False


