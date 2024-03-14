import sys
num=[list(map(int,sys.stdin.readline().split())) for _ in range(9)]
max=0
for i in range(9):
    for j in range(9):
        if num[i][j]>=max:
            max=num[i][j]
            a=i
            b=j
print(max,a,b)