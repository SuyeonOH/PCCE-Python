import sys
n=int(sys.stdin.readline())
n_list=[]
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

#bubble sort
for i in range(len(n_list)-1,0,-1):
    for j in range(i):
        if n_list[j]>n_list[j+1]:
            n_list[j],n_list[j+1]=n_list[j+1],n_list[j]

for i in range(len(n_list)):
    print(n_list[i])