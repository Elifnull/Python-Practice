from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def turn_left():
    tim.lt(10)


def turn_right():
    tim.rt(10)


def move_back():
    tim.bk(20)


def reset():
    tim.reset()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_back, "s")
screen.onkey(reset, "c")

screen.exitonclick()
