from turtle import Turtle, Screen
import turtle as t
import random

###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image2.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(158, 152, 148), (147, 149, 154), (130, 84, 76), (70, 117, 150), (224, 78, 98), (15, 21, 30), (146, 148, 147), (83, 19, 9), (174, 139, 146), (114, 36, 27), (108, 120, 159), (1, 60, 143), (128, 87, 94), (102, 105, 102), (31, 19, 26), (4, 9, 8), (187, 93, 81), (186, 188, 203), (132, 130, 119), (100, 41, 51), (197, 195, 179), (77, 68, 41), (125, 129, 126), (112, 132, 140)]
# print(rgb_colors)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.pensize(10)
tim.speed("fastest")
t.colormode(255)
x = -220
y = -220
gap = 50
tim.setpos(x,y)

size = 10
for _ in range(size):
    for _ in range(size):
        tim.color(random.choice(color_list))
        tim.down()
        tim.dot()
        tim.up()
        tim.forward(gap)

    y += gap

    tim.setpos(x, y)
    tim.up()


screen = Screen()
screen.exitonclick()