import turtle
import colorsys

s = turtle.Screen()
s.bgcolor("black")

t = turtle.Pen()
t.speed(12)

h = 0
n = 36

for i in range(100):
    
    c = colorsys.hsv_to_rgb(h, 0.7, 0.9)
    
    t.width(i//50+i)
    t.pencolor(c)
    t.left(119)
    t.fillcolor(c)
    t.forward(i)
    t.circle(i,30)
    t.begin_fill()
    
    for j in range(9):
        
        t.right(255)
        t.forward(i*0.7)
        
    t.end_fill()
    
    t.forward(i*1.5)
    t.circle(i,200)
    
    h += 1/n
    
turtle.done()