import random

lotto_num=[]
count =0

while True:
    num=random.randint(1,45)
    if num not in lotto_num: #멤버십 연산자
        lotto_num.append(num)
        count +=1

        if count==6:
            break

for lotto in lotto_num:
    print(lotto, end=' ')