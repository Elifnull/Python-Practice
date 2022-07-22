from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
turtle_colors = ["DarkOrchid", "yellow", "purple", "CornflowerBlue", "orange", "pink", "skyblue", "navy blue", "DeepSkyBlue", "SlateGray", "SeaGreen"]
for num in range(3, 11):
    degree = 360 / num
    turns = 360/degree
    turns_left = 0
    tim.color(random.choice(turtle_colors),random.choice(turtle_colors))
    while turns_left < turns:
        tim.right(degree)
        tim.forward(100)
        turns_left += 1

screen = Screen()
screen.screensize(2000,1500)
screen.exitonclick()
