import turtle as t1
import math
import random

t1.setup(width= 800, height=800)
t1.shape('turtle')
t1.color('orange')
t1.bgcolor('steelblue')
t1.penup()

t1.turtlesize(3)

t2=t1.clone()
t2.color('tomato')

t1.goto(-400, 300)
t2.goto(-400,-300)

while True:
    t1.forward(random.randint(1,100))
    t2.forward(random.randint(1,100))

    if t1.xcor() > 400 :
        t1.goto(0,0)
        t1.write("           winner", font=('Arial',16))
        break
    elif t2.xcor() > 400 :
        t2.goto(0,0)
        t2.write("           winner", font=('Arial', 16))
        break

t1.exitonclick()

