import turtle
import turtle
import time
import random
print("This program draws the shapes based on the number you enter in a uniform pattern.")
num=input("Enter the side number of the shape you want to draw:")
if num.isdigit():
    squares=int(num)
angle=180-180*(squares-2)/squares
turtle.up
x=0
y=0
turtle.setpos(x,y)
numshapes=8
for x in range(numshapes):
    turtle.color(random.random(),random.random(),random.random())
    x+=5
    y+=5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print(turtle.pos())
        turtle.up()
        turtle.end_fill()
time.sleep(11)
turtle.bye()