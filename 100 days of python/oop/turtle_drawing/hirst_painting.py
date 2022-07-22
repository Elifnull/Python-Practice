import random
import colorgram
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)  # sets the rbg mode to accept a range from 0-255


def color_extraction_array(image_name, colour_count):
    array_of_colors = []
    colors = colorgram.extract(image_name, colour_count)
    for value in range(colour_count):
        array_of_colors.append(colors[value].rgb)
    print(array_of_colors)
    return array_of_colors


color_array = color_extraction_array("image.jpeg", 19)
print(color_array[0])
hi_turtle = Turtle()


hi_turtle.speed("fastest")
for num in range(100):
    hi_turtle.color(random.choice(color_array))
    hi_turtle.circle(100)
    hi_turtle.rt(5)

screen = Screen()
screen.exitonclick()

