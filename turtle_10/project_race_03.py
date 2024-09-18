import random
from turtle import Turtle, Screen

def draw_turtles(t_name, t_colour, t_y):
    t_name = Turtle()
    t_name.penup()
    t_name.goto(-300, t_y)
    t_name.pendown()
    t_name.shape('turtle')
    t_name.color(t_colour)
    t_name.shapesize(1.5)
    return t_name

game_end = False


def move_func():
    if not game_end:
        black_turtle.forward(15)


my_turtle = Turtle()
my_turtle.penup()
my_turtle.speed('fastest')

# Screen Setup
my_screen = Screen()
my_screen.setup(800, 500)
my_screen.title('Turtle race')
my_screen.bgcolor('green')

# Heading
my_turtle.penup()
my_turtle.goto(-70, 205)
my_turtle.color('white')
my_turtle.write('Turtle race', font=('Arial', 20, 'bold'))

# The Floor
my_turtle.goto(-350,200)
my_turtle.pendown()
my_turtle.fillcolor('chocolate')
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()

# finish line
my_turtle.goto(250, 200)
my_turtle.right(90)
my_turtle.forward(400)

# draw turtles
blue_turtle = draw_turtles(t_name='blue_turtle', t_colour='cyan', t_y=150)
green_turtle = draw_turtles(t_name='green turtle', t_colour='green', t_y=50)
red_turtle = draw_turtles(t_name='red turtle', t_colour='red', t_y=-50)
black_turtle = draw_turtles(t_name='black turtle', t_colour='black', t_y=-150)

# moving da turtles
my_screen.listen()
my_screen.onkey(move_func, 'Right')


while True:
    blue_turtle.forward(random.randint(1,5))
    green_turtle.forward(random.randint(1, 5))
    red_turtle.forward(random.randint(1, 5))
    # black_turtle.forward(random.randint(1, 10))
    if blue_turtle.xcor()> 235:
        winner = blue_turtle
        break
    elif green_turtle.xcor()> 235:
        winner = green_turtle
        break
    elif red_turtle.xcor()> 235:
        winner = red_turtle
        break
    elif black_turtle.xcor()> 235:
        winner = black_turtle
        break

# celebrate with the winner
game_end = True
winner.shapesize(2.5)
winner.penup()
for i in range(5):
    winner.circle(20)


my_screen.exitonclick()
