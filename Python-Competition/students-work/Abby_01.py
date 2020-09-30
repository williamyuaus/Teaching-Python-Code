import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

# Draws a circle at the given x,y coordinates
def draw_circle(x,y):
    colour = random.choice(["red","blue","purple","pink","aqua","green","orange","yellow"]) # Picks a random colour to draw the shape
    turtle.hideturtle()
    t.color(colour)
    t.pensize(10)
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.rt(90)
    t.fd(75)
    t.lt(90)
    t.pendown()
    t.circle(50)

# Draws a triangle at the given x,y coordinates
def draw_triangle(x,y):
    colour = random.choice(["red", "blue", "purple", "pink", "aqua", "green", "orange", "yellow"]) # Picks a random colour to draw the shape
    turtle.hideturtle()
    t.color(colour)
    t.pensize(10)
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.bk(37.5)
    t.pendown()
    t.fd(75)
    t.lt(120)
    t.fd(75)
    t.lt(120)
    t.fd(75)

# Draws a square at the given x,y coordinates
def draw_square(x,y):
    colour = random.choice(["red", "blue", "purple", "pink", "aqua", "green", "orange", "yellow"]) # Picks a random colour to draw the shape
    turtle.hideturtle()
    t.color(colour)
    t.pensize(10)
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.rt(90)
    t.fd(25)
    t.lt(90)
    t.bk(25)
    t.pendown()
    for i in range(4):
        t.fd(50)
        t.lt(90)

# The main function that runs everything
# Asks the user what shape to draw and lets them click on the canvas where to draw the shape and returns that x,y of click to the function of the shape they chose
def main():
    while True:
        shape = input("Choose a shape to draw (circle/triangle/square): ")
        if shape == "circle":
            print("Click on the canvas where you want to draw the circle")
            s.onscreenclick(lambda x, y: draw_circle(x,y))
            turtle.mainloop()
            quit()
        elif shape == "triangle":
            print("Click on the canvas where you want to draw the triangle")
            s.onscreenclick(lambda x, y: draw_triangle(x,y))
            turtle.mainloop()
            quit()
        elif shape == "square":
            print("Click on the canvas where you want to draw the square")
            s.onscreenclick(lambda x, y: draw_square(x,y))
            turtle.mainloop()
            quit()
        else:
            print("Invalid shape, try again")

# Runs the main program
main()