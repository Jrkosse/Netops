from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

for i in range(0,15):
    timmy.left(90)
    timmy.forward(100)
    timmy.right(180)
    timmy.forward(100)
    
my_screen = Screen()
my_screen.exitonclick()