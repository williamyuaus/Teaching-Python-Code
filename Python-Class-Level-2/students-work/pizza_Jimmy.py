import turtle

x = 0
BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
PINEAPPLE_COLOR = "#FFEC89"
CHEESE_COLOR = "#FBC70F"
HAM_COLOR = "#FFC0CB"
HAM_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Pizza")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")


def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x,y):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.down()

def draw_ham(size, line_color, fill_color):
    
    for z in HAM_LOCATIONS:
       move_turtle(z[0], z[1])
       my_turtle.color(HAM_COLOR)
       my_turtle.fillcolor(HAM_COLOR)
       my_turtle.begin_fill()
       for z in range(0,4):
           my_turtle.forward(size)
           my_turtle.left(90)
       my_turtle.end_fill()
           
        
    

    

draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 20)
draw_circle(130, SAUCE_COLOR, CHEESE_COLOR)
draw_ham(10, HAM_COLOR, HAM_COLOR)
move_turtle(0,150)
my_turtle.color(BACKGROUND_COLOR)
for z in range (0,8): 
   my_turtle.left(45)
   my_turtle.forward(150)
   move_turtle(0,150)

my_turtle.hideturtle()


