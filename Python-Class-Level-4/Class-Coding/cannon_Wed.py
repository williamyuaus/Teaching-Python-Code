from random import *
from turtle import *
from base import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

def move():
    if randrange(10) == 0:
        y = randrange(-199, 199)
        target = vector(199, y)
        targets.append(target)

    for target in targets:
        target.x -= 3

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    for target in targets:
        if abs(target - ball) < 13:
            targets.remove(target)

    draw()
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

    
        