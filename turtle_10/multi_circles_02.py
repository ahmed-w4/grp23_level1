from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('red')
random_colors_list = ['red','blue','green','purple', 'yellow', 'black', 'brown', 'grey']

for i in range(11): # import module random and it chooses random values from a list
    my_turtle.circle(100)
    my_turtle.left(10)
    my_turtle.color(random.choice(random_colors_list))

my_screen = Screen()
my_screen.exitonclick()