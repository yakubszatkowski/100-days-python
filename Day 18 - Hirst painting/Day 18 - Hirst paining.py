# import colorgram
# colors = colorgram.extract('image.jpg', 10)
#
# list_of_colors = []
# for color in colors:
#     # red = color.rgb.r; green = color.rgb.b; blue = color.rgb.b
#     color_pack = (color.rgb.r, color.rgb.g, color.rgb.b)
#     list_of_colors.append(color_pack)
#
# print(list_of_colors)
# 10 raw_data 10 spots
# 20 size spots
# 50 apart

import turtle as t
from random import choice

list_of_colors = [(153, 151, 148), (154, 150, 152), (132, 151, 142), (198, 12, 32), (150, 237, 17), (39, 76, 189),
                  (38, 217, 68), (238, 227, 5), (129, 159, 46), (27, 40, 157)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
y_position = -200
tim.hideturtle()

for i2 in range(10):
    tim.setposition(-250, y_position)
    y_position += 50
    for i1 in range(10):
        tim.dot(20, choice(list_of_colors))
        tim.forward(50)

t.exitonclick()

