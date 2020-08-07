import turtle as t
from random import randint, random
t.Screen().bgcolor('dark blue')

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

while True:
    ranCol = (random(), random(), random())
    ranPts = randint(2, 5) * 2 + 1
    ranSize = ?
    ranX = ?
    ranY = ?

    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
