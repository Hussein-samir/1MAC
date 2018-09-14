import turtle
import time

myClass = turtle.Turtle()

window = turtle.Screen()
window.bgcolor("red")

myClass.shape("turtle")
myClass.speed(100)
myClass.color("White")

square_length = 120
def draw_square(length):
    n = 0
    while n<4:
        myClass.forward(length)
        myClass.right(90)
        n += 1
d=0
print time.ctime()
while d<100:
    draw_square(square_length)
    myClass.left(3.6)
    d += 1
print time.ctime()
mySecClass = turtle.Turtle()

mySecClass.sety(200)
mySecClass.circle(100)
turtle.exitonclick()