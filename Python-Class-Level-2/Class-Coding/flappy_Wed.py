from random import *
from turtle import *
from base import vector

bird = vector(0, 0)
balls = []

def tap(x, y):
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')
