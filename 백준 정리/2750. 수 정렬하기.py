import sys
num=int(sys.stdin.readline())
num_list=[]
for _ in range(num):
    num_list.append(int(sys.stdin.readline()))

#bubble sort 이용
for i in range(len(num_list)-1,0,-1):
    for j in range(i):
        if num_list[j]>num_list[j+1]:
            num_list[j],num_list[j+1]=num_list[j+1],num_list[j]

for i in range(len(num_list)):
    print(num_list[i])