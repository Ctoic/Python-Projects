# creating a heart using turtle graphics
import turtle
import time
import random

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Heart")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create the heart
heart = turtle.Turtle()
heart.speed(0)
heart.shape("square")
heart.color("black")
heart.penup()
heart.goto(0, 0)
heart.direction = "stop"

# Define the functions for moving the heart
def move():
    if heart.direction == "up":
        y = heart.ycor()
        heart.sety(y + 20)
    if heart.direction == "down":
        y = heart.ycor()
        heart.sety(y - 20)
    if heart.direction == "right":
        x = heart.xcor()
        heart.setx(x + 20)
    if heart.direction == "left":
        x = heart.xcor()
        heart.setx(x - 20)

def go_up():
    if heart.direction != "down":
        heart.direction = "up"

def go_down():
    if heart.direction != "up":
        heart.direction = "down"

def go_right():
    if heart.direction != "left":
        heart.direction = "right"

def go_left():
    if heart.direction != "right":
        heart.direction = "left"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if heart.xcor() > 290 or heart.xcor() < -290 or heart.ycor() > 290 or heart.ycor() < -290:
        time.sleep(1)
        heart.goto(0, 0)
        heart.direction = "stop"

    move()

    time.sleep(delay)

wn.mainloop()


