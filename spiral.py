import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")


def polygon(n, size=80):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(100)

colors = ['orange', 'cyan', 'blue', 'green', 'red']

size = 40

for i in range(0, 60):
    turtlePen.color(colors[i % 5])
    polygon(4, size)
    turtlePen.left(5)
    size = size + 3

window.mainloop()