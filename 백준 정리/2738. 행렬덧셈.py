import sys
n,m=map(int,sys.stdin.readline().split())
array1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
array2=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=[[0]*m]*n
# print(array1,array2,result,end='\n')
for i in range(n):
    for j in range(m):
        result[i][j]=array1[i][j]+array2[i][j]
        print(result[i][j], end=' ')
    print()

