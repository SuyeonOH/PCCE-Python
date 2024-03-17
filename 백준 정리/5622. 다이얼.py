import sys
word=sys.stdin.readline().rstrip()#WA
dial={"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
time=0
for d in word:#W , A
    for i,t in dial.items(): #key, value 쌍 얻기  # WXYZ, 10
        if d in i:
            time+=t
print(time)