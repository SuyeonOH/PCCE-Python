import sys
n,k=map(int,sys.stdin.readline().split())
x=list(map(int,sys.stdin.readline().split()))
#[100 76 85 93 98] bubble sort 이용
for i in range(len(x)-1,0,-1):
    for j in range(i):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)
print(x[len(x)-k])#5 -> 2