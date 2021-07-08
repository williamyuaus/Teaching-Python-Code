"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
from turtle import *
from base import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
bosses = []
writer = Turtle(visible=False)

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    for boss in bosses:
        goto(boss.x, boss.y)
        dot(40, 'green')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
        boss = vector(200, y)
        bosses.append(boss)

    for target in targets:
        target.x -= 1.5

    for boss in bosses:
        boss.x -= 10

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # dupe = targets.copy()
    # targets.clear()

    # for target in dupe:
    #     if abs(target - ball) > 13:
    #         targets.append(target)

    for target in targets:
        if abs(target - ball) < 13:
            targets.remove(target)
            ball.x = -199
            ball.y = -199
            speed.x = -10
            speed.y = -10

    for boss in bosses:
        if abs(boss - ball) < 23:
            bosses.remove(boss)
            clear
            speed.x = 5

    draw()

    for target in targets:
        if not inside(target):
            writer.goto(30, 30)
            writer.color('black')
            writer.write('Game Over',font=("Verdana", 15, "normal"))
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()