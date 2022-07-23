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


def hirst_painting(height, width): #refactored program so that it works in x,y coordinates instead of using set heading
    """accepts Height and width to determin hirst painting parameters"""
    for num in range(height):
        hi_turtle.penup()
        y_coordinate_value = (num * 50 -220)
        hi_turtle.sety(y_coordinate_value)
        for number in range(width):
            hi_turtle.setx((number * 50) - 220)
            hi_turtle.dot(20, random.choice(color_array))


hirst_painting(10, 10)

hi_turtle.hideturtle() # hides turtle at the end
screen = Screen()
screen.exitonclick()

