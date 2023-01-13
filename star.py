from turtle import *
import turtle 

painting = turtle.Turtle()

painting.pencolor("red")

for x in range(60):
    painting.forward(60)
    painting.left(133)
    
painting.pencolor("blue")
for x in range(60):
    painting.forward(100)
    painting.left(133)
    
turtle.done()