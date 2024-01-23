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

left = (int(input("왼쪽 배팅 금액(원) : ")))
right = (int(input("오른쪽 배팅 금액(원) : ")))

for i in range(10) :
    # 두쪽 중 하나가 100만원 이상의 금액이면
    if left >=1000000 or right <= 1000000 :
        #확률조작
        if left > right :
            t.forward(random.randint(-30,60))
        else :
            t.forword(random.ranint(-60, 30))
    #100만원 이하의 경우에는 원래의 확률대로
    else :
            t.forward(random.randint(-50,50))

    time.sleep(1)



if t.xcor() > 0 :
    t.write("right", font = ('Arial', 16))
elif t.xcor() == 0 :
    t.write("0", font= ("Arial", 15 ))
else :
    t.write("left", font=("Arial", 16))

t.exitonclick()