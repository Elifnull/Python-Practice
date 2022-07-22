import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(17)
turtle_colors = ["DarkOrchid", "yellow", "purple", "CornflowerBlue", "orange", "pink", "skyblue", "navy blue",
                "DeepSkyBlue", "SlateGray", "SeaGreen"]
for _ in range(100):
    turn_position_number = random.randint(1, 4)
    turn_angle = 90 * turn_position_number
    tim.color(random_colour(), random_colour())
    tim.rt(turn_angle)
    tim.fd(30)

screen = Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
