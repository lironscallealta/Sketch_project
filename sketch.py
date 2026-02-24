#Etch A Sketch project
from turtle import Turtle, Screen

#Objects
#names
callejas = Turtle()
screen = Screen()

def f():
    callejas.fd(10)

def turn():
    callejas.speed("fastest")
    callejas.left(180)

def back():
    callejas.back(10)

#one way to do it
def turn_right():
    callejas.right(10)
#another creative way to do it as well
def turn_left():
    moving_left = callejas.heading() + 10
    callejas.setheading(moving_left)

def going_home():
    callejas.speed("normal")
    callejas.penup()
    callejas.clear()
    callejas.home()
    callejas.pendown()




screen.listen()
screen.onkey(key = "4", fun= back)
screen.onkey(key = "s", fun= back)
screen.onkey(fun=turn,key= "5")
screen.onkey(fun=turn,key= "x")
screen.onkey(fun=f,key= "6")
screen.onkey(fun=f,key= "w")
screen.onkey(fun=turn_left,key= "8")
screen.onkey(fun=turn_left,key= "a")
screen.onkey(fun=turn_right,key= "2")
screen.onkey(fun=turn_right,key= "d")
screen.onkey(fun=going_home,key= "c")

screen.exitonclick()
