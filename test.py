import math
import turtle as t
import time
import random

t.setup(width= 800, height=800)
t.shape('turtle')
t.color('orange')
t.bgcolor('steelblue')

t.goto(0,400)
t.goto(0,-400)
t.goto(0,0)

t.speed(1)

t.penup()

for i in range(10) :
    t.forward(random.randint(-50,50))
    time.sleep(1)

if t.xcor() > 0 :
    t.write("right", font = ('Arial', 16))
elif t.xcor() == 0 :
    t.write("0", font= ("Arial", 15 ))
else :
    t.write("left", font=("Arial", 16))

t.exitonclick()