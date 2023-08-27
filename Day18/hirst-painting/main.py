# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

import turtle as t
import random
color_list = [(181, 171, 162), (185, 177, 180), (211, 194, 157), (159, 78, 48), (153, 179, 158), (40, 109, 133), (156, 176, 185), (48, 126, 90), (212, 182, 177), (175, 150, 44), (205, 183, 187), (137, 70, 80), (153, 23, 31), (142, 29, 21), (204, 91, 67), (12, 99, 77), (70, 45, 35), (94, 148, 110), (181, 198, 188), (73, 148, 167), (22, 64, 86), (63, 44, 50), (193, 77, 85), (11, 89, 104), (186, 191, 199), (168, 202, 208)]

tim = t.Turtle()
tim.up()
tim.speed("fastest")
start_x_pos = -200
start_y_pos = -200
tim.setpos(start_x_pos,start_y_pos) # starting pos

tim.screen.colormode(255)

for rows in range(10):
    for columns in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    start_y_pos += 50
    tim.setpos(start_x_pos,start_y_pos)


screen = t.Screen()
screen.exitonclick()