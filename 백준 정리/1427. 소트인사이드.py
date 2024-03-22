import sys
num=int(sys.stdin.readline())
n_list=[]
while (num!=0):
    n_list.append(num%10)
    num//=10

for i in range(len(n_list)-1,0,-1):
    for j in range(i):
        if n_list[j] > n_list[j+1]:
            n_list[j],n_list[j+1]=n_list[j+1],n_list[j]
print(n_list)
for i in range(len(n_list)-1,-1,-1):
    print(n_list[i], end='')