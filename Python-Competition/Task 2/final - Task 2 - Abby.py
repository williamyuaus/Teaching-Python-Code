# A possible problem of this program is that on slow computers, the coloured squares will appear slightly longer, and on fast computers, the coloured squares will appear slightly shorter
# A tkinter error will appear after you quit/get rid of the turtle screen. It does not affect the program, but I do not know how to fix it.

# Files and methods imported
import turtle
import random
import time
import winsound


# Ascii art dice, red and yellow
redl = [''' ________
|        |
|  RED!  |
|________|''']

yellowl = [''' ________
|        |
| YELLOW!|
|________|''']

# The global variables
points = 0  # The points variable that keeps track of how many the user scored
square_x = [None,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200,-300,-200,-100,0,100,200]  # The x coordinates of the bottom left corner of each square of the 6 x 6 grid. Can be retrieved by indexing. E.g. to get the x coordinates of square 10 you would do square_x[10]
square_y = [None,200,200,200,200,200,200,100,100,100,100,100,100,0,0,0,0,0,0,-100,-100,-100,-100,-100,-100,-200,-200,-200,-200,-200,-200,-300,-300,-300,-300,-300,-300]  # The y coordinates of the bottom left corner of each square of the 6 x 6 grid. Can be retrieved by indexing. E.g. to get the y coordinates of square 10 you would do square_y[10]
status = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # The status of each square of the 6 x 6 grid. 0 is empty, 1 is yellow, -1 is red. status[0] is the index of the square which is either red or yellow.


s = turtle.getscreen()  # Assigning the turtle screen as 's'
t = turtle.Turtle()  # Assigning the turtle as 't'


# Draws a yellow square from the bottom left corner coordinates of a square given by square_x and square_y, indexed by status[0]
def draw_yellow_square():
    t.speed(0)
    t.penup()
    t.goto(square_x[status[0]], square_y[status[0]])
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()


# Draws a red square from the bottom left corner coordinates of a square given by square_x and square_y, indexed by status[0]
def draw_red_square():
    t.speed(0)
    t.penup()
    t.goto(square_x[status[0]], square_y[status[0]])
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()


# Draws an empty square from the bottom left corner coordinates of a square given by square_x and square_y, indexed by status[0]
def draw_empty_square():
    t.speed(0)
    t.penup()
    t.goto(square_x[status[0]], square_y[status[0]])
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()


# Picks a random square and makes it red or yellow
def random_square():
    l1 = [1,2]
    l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    draw_empty_square()  # Draws an empty square over the coloured square it drew last
    status[status[0]] = 0  # Makes the status of the last coloured square 0
    red_yellow = random.choice(l1)  # Chooses to draw the next square red or yellow. 1 is yellow, 2 is red. Kind of like a dice
    ran_square = random.choice(l2)  # Chooses a square to draw the next coloured square in. Kind of like a dice
    status[0] = ran_square  # Makes status[0] the index of the next coloured square
    if red_yellow == 1:  # Draws yellow square and makes the index of the square in status 1
        print(yellowl[0])  # Prints yellow dice
        status[ran_square] = 1
        draw_yellow_square()
    else:  # Draws red square and makes the index of the square in status -1
        print(redl[0])  # Prints red dice
        status[ran_square] = -1
        draw_red_square()


#  Draws the board of the game (6x6). Each square is 100 pixels by 100 pixels.
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


# Turns the x,y coordinates of the user's click into the square they clicked on.
def get_square(x, y):
    xnew = int((x + 300) // 100 + 1)
    ynew = int(6 - (y + 300) // 100)
    return (ynew - 1) * 6 + xnew


# Prints welcome and instructions. Has time between printing the next row of text so that the user can read it carefully.
def intro():
    print("Welcome to Click-a-game!")
    time.sleep(0.5)
    print("The aim is to click on the yellow square as fast as you can before it disappears, and avoid the red squares!")
    time.sleep(1.5)
    print("A point is given every time you click on a yellow square, and a point is taken every time you click on a red square!")
    time.sleep(1.5)
    print("Good luck!")


# This function runs everytime the user has clicked on the screen
def semi_main(x,y):
    global points
    square = get_square(x,y)
    if status[square] == 1:  # If the square the user clicked on is 1 (i.e it is yellow), one point is added and it plays a high pitched beep
        points = points + 1
        winsound.Beep(2000, 100)
        # Make square empty again
    elif status[square] == -1:  # If the square the user clicked on is -1 (i.e it is red), one point is deducted and it plays a low pitched beep
        points = points - 1
        winsound.Beep(300, 100)
        # Make square empty again
    else:  # The user clicked on an empty square, nothing happens, but will print the user's points anyway
        pass
    print("Points:", points)  # Prints points everytime the user clicks, regardless where


# Main function
def main():
    draw_board()
    i = 1  # This is assigned to make the coloured square last longer. However, a possible problem of this is that on slow computers, the coloured squares will appear longer, and on fast computers, the coloured squares will appear shorter
    while True:
        s.onscreenclick(lambda x, y: semi_main(x, y))  # Detects the user's clicks and runs the semi main function with the coordinates of the user's click as the x,y arguments of the semi main function
        i = i + 1
        if i == 26000:  # When i == 26000, a new square turns coloured and the old one is emptied (the random_square() function)
            random_square()
            i = 1  # i is reset to 1


# Runs the intro function, then the main
intro()
main()