import turtle
import random
import time
import winsound


points = 0
square_x = [None,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200]
square_y = [None,200,200,200,200,200,200,100,100,100,100,100,100,0,0,0,0,0,0,-100,-100,-100,-100,-100,-100,-200,-200,-200,-200,-200,-200,-300,-300,-300,-300,-300,-300]
status = [None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 0 is empty, 1 is yellow, -1 is red


s = turtle.getscreen()
t = turtle.Turtle()


def draw_yellow_square(squarei):
    t.speed(0)
    t.penup()
    t.goto(square_x[squarei],square_y[squarei])
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()

def draw_red_square(squarei):
    t.speed(0)
    t.penup()
    t.goto(square_x[squarei], square_y[squarei])
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()


def random_square():
    l1 = [1,2]
    l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    red_yellow = random.choice(l1)
    ran_square = random.choice(l2)
    if red_yellow == 1:
        status[ran_square] = 1
        draw_yellow_square(ran_square)
    else:
        status[ran_square] = -1
        draw_red_square(ran_square)


def draw_board():
    turtle.hideturtle()
    t.pensize(10)
    t.speed(0)
    for i in range(4):
        t.fd(300)
        t.bk(300)
        t.rt(90)
    t.goto(-300, 0)
    t.lt(90)
    t.fd(300)
    t.bk(300)
    for i in range(6):
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.fd(300)
        t.bk(300)
    t.rt(180)
    t.fd(300)
    t.bk(300)
    for i in range(6):
        t.rt(90)
        t.fd(100)
        t.lt(90)
        t.fd(300)
        t.bk(300)
    t.fd(300)
    t.lt(90)
    t.fd(600)
    t.bk(600)
    for i in range(6):
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.fd(600)
        t.bk(600)


def get_square(x, y):
    xnew = int((x + 300) // 100 + 1)
    ynew = int(6 - (y + 300) // 100)
    if xnew < 1 or xnew > 6:
        raise Exception("Click out of range")
    if ynew < 1 or ynew > 6:
        raise Exception("Click out of range")
    return (ynew - 1) * 6 + xnew


def intro():
    print("Welcome to Click-a-game!")
    print("The aim is to click on the yellow square as fast as you can, and avoid the red squares!")
    print("A point is given every time you click on a yellow square, and a point is taken every time you click on a red square!")
    print("Good luck!")


def semi_main(x,y):
    random_square()
    square = get_square(x,y)
    if status[square] == 1:
        points = points + 1
        winsound.Beep(2000, 100)
        # Make square empty again
    elif status[square] == -1:
        points = points - 1
        winsound.MessageBeep()
        # Make square empty again
    else:
        pass


def main():
    intro()
    draw_board()
    s.onscreenclick(lambda x, y: semi_main(x, y))
    turtle.mainloop()

main()
