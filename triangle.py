import colorsys
import turtle
from turtle import *

turtle.title("triangle")
bgcolor("black")
penup()
goto(-200, -100)
pendown()
speed(10)

a = 400
h = 0
n = 100


def triangle():
    global a, n, h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h, 1, 0.6)
        h = h + (1 / n)
        color(c)
        forward(a)
        left(120)
        a = a - 10

triangle()
triangle()

hideturtle()
turtle.done()