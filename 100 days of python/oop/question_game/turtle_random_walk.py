from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fast")
tim.pensize(10)
turtle_colors = ["DarkOrchid", "yellow", "purple", "CornflowerBlue", "orange", "pink", "skyblue", "navy blue", "DeepSkyBlue", "SlateGray", "SeaGreen"]
for _ in range(0, 100):
    turn_position_number = random.randint(1, 4)
    turn_angle = 90 * turn_position_number
    tim.color(random.choice(turtle_colors), random.choice(turtle_colors))
    tim.rt(turn_angle)
    tim.fd(30)

screen = Screen()
screen.screensize(2000, 1500)
screen.exitonclick()
