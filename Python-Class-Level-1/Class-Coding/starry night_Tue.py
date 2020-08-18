import turtle
from random import randint, random

turtle.Screen().bgcolor('dark blue')

def draw_star(points, size, col, x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    angle = 180 - (180 / points)
    turtle.color(col)
    turtle.begin_fill()
    for i in range(points):
        turtle.forward(size)
        turtle.right(angle)
    turtle.end_fill()

while True:
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    ranCol = (1, 0, 0)
    draw_star(5, 100, ranCol, ranX, ranY)
