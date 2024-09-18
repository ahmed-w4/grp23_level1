import random
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.speed('fast')
my_turtle.shape('turtle')
my_turtle.penup()

random_colors_list = ['red','blue','green','purple', 'yellow', 'black', 'brown', 'grey']

my_turtle.goto(0, -100)
my_turtle.pendown()
my_turtle.color('yellow')

for i in range(3, 11):
    angle = 360 / i
    my_turtle.color(random.choice(random_colors_list))
    for j in range(i):
        my_turtle.forward(100)
        my_turtle.left(angle)


#
# my_turtle.color('green')
# for s in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)
#
# for p in range(5):
#     my_turtle.forward(100)
#     my_turtle.left(72)
# my_turtle.color('blue')
#
# for h in range(6):
#     my_turtle.forward(100)
#     my_turtle.left(60)
#
# for heptagon in range(7):
#     my_turtle.forward(100)
#     my_turtle.left(360/7)
# my_turtle.color('red')
# for o in range(8):
#     my_turtle.forward(100)
#     my_turtle.left(45)
# my_turtle.color('yellow')
# for n in range(9):
#     my_turtle.forward(100)
#     my_turtle.left(40)
# my_turtle.color('red')
# for d in range(10):
#     my_turtle.forward(100)
#     my_turtle.left(36)


my_screen = Screen()
my_screen.exitonclick()