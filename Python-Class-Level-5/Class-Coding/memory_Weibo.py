from random import *
from turtle import *
from base import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x,y)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
draw()
done()
