import sys
c_list=[1,1,2,2,2,8]
num_list=list(map(int,sys.stdin.readline().split()))
result=[]
for i in range(len(num_list)):
    result.append(str(c_list[i]-num_list[i]))

print(' '.join(result))