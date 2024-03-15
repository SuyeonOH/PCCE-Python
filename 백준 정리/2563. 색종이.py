import sys
n=int(sys.stdin.readline())
array=[[0]*100 for _ in range(100)]

for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())

    for i in range(b,b+10):
        for j in range(a,a+10):
            array[i][j]=1
result=0
for k in range(100):
    result+=array[k].count(1)
print(result)