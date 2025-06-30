""" Simple Snake Game in Python"""

import turtle                                   #Turtle module: Used for drawing shapes and graphics 
import time
import random

delay =  0.1

score = 0                                                # Score
high_score = 0

wn = turtle.Screen()                                       # Setup 
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)                                       #Turns off the animation on the screen

head = turtle.Turtle()                                          # Snake head
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()                                             #Snake food
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []                                                      # Segment List

pen = turtle.Turtle()                                                 # Pen 
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to make the head to move
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left" 

def go_right():
    if head.direction != "left":
        head.direction = "right"       

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)    

# Keyboard Bindings     
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.listen()

# main game loop
while True:
    wn.update()
    
    if head.xcor()> 290 or head.xcor()< -290 or head.ycor()> 290 or head.ycor()< -290:         # Border Collision
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        for segment in segments:                           # Hide the segments
            segment.goto(1000, 1000)
            
        segments.clear()                                  # CLear the segments list
        
        score = 0                                         # Reset the score
        
        delay = 0.1                                       # Reset the delay 
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
                    
    if head.distance(food) < 20:                          # Checking for collision with the food
        x = random.randint(-290 ,290)                     # Move the food to a random spot
        y = random.randint(-290 ,290)
        food.goto(x,y)
    
        new_segment = turtle.Turtle()                      # Add a new segment
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.001                                    # Shorten the delay
        
        score += 10                                       # Increase the score
        
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    for index in range(len(segments)-1, 0, -1):                # Make the end segments first in reverse order
        x = segments[index-1].xcor()
        y = segments[index-1].ycor() 
        segments[index].goto(x, y)
        
    if len(segments) > 0:                                     # Move segment 0 to where the head is
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    for segment in segments:
        if segment.distance(head) < 20:                       # Head Collisions with the body segments
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for segment in segments:                            # Hide the segments
                segment.goto(1000, 1000)
                
            segments.clear()                                   # Clear the segments list
            
            score = 0                                         # Reset the score
        
            delay = 0.1                                        # Reset the delay
        
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(delay)

wn.mainloop()

