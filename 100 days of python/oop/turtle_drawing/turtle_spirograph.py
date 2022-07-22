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
turn_angle = 0


def draw_spirograph(gap):
    for _ in range(0, 360, gap):
        tim.color(random_colour(), random_colour())
        tim.rt(gap)
        tim.circle(100)


draw_spirograph(5)

screen = Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
