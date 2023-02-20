import turtle 
import time 
import random 


# creating screen 
wn = turtle.Screen()
wn.title("Tetris")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# creating the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# creating the player
player = turtle.Turtle()
player.color("black")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0, -250)

# creating the player's movement
playerspeed = 15

