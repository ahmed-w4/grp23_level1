from turtle import Turtle, Screen

# turtle_01 = Turtle()
# turtle_01.forward(100)
#
# turtle_02 = Turtle() # go backward and change curser direction
# turtle_02.left(180)
# turtle_02.forward(100)

turtle_q = Turtle()
# turtle_q.forward(250)
# turtle_q.left(90)
# turtle_q.forward(200)
# turtle_q.left(90)
# turtle_q.forward(250)
# turtle_q.left(90)
# turtle_q.forward(200)

turtle_q.shape('turtle')
turtle_q.color('black')
turtle_q.fillcolor('green')
turtle_q.begin_fill()

for i in range(2):
    turtle_q.forward(250)
    turtle_q.left(90)
    turtle_q.forward(200)
    turtle_q.left(90)
turtle_q.end_fill()

turtle_q.penup()
turtle_q.goto(-200, 100)

turtle_q.shape('square')
# turtle_q.stamp()
# turtle_q.forward(100)
# turtle_q.stamp()
# turtle_q.forward(100)
# turtle_q.stamp()

for i in range(3):
    turtle_q.stamp()
    turtle_q.forward(100)


turtle_q.shape('turtle')
turtle_q.goto(-100, -200)
turtle_q.pendown()
turtle_q.circle(50)


my_screen = Screen()
my_screen.exitonclick()



