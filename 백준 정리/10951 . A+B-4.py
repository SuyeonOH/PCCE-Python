# import sys

# while True:
#     try:
#         a,b = map(int,sys.stdin.readline().split())
#         print(a+b)
#     except:
#         break
import sys

n=int(sys.stdin.readline())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))