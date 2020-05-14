import turtle


BACKGROUND_COLOR = "#9EC388"

CRUST_COLOR = "#000000"

SAUCE_COLOR = "#6F8287"

PINEAPPLE_COLOR = "#FFEC89"

CHEESE_COLOR = "#FBC70F"

PEPPERONI_LOCATIONS = [
    [-70,105],
    [-85,175],
    [-25,50],
    [-15,100],
    [-30,205],
    [15,50],
    [20,200],
    [60,156],
    [71,215],
    [80,90],
    [95,150],
    [150,150],
    [-150,225],
    [-110,40],
    [190,30],
    [170,100]

    ]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Pizza")

my_turtle=turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(sidelenth, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    for x in range (0,2):
        my_turtle.forward(sidelenth)
        my_turtle.left(90)
    my_turtle.forward(sidelenth*2)
    for y in range(0,2):
        my_turtle.left(90)
        my_turtle.forward(sidelenth)
    my_turtle.end_fill()

def move_turtle(x,y):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.down()

draw_circle(300, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 25)
draw_circle (250, SAUCE_COLOR, CHEESE_COLOR)

for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(0,150)
my_turtle.color(BACKGROUND_COLOR)
for z in range (0,8):
    my_turtle.forward(300)
    move_turtle(0,150)
    my_turtle.left(45)

