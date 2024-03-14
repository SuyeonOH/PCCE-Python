import sys
w=[]
for _ in range (5):
    a=sys.stdin.readline().rstrip()
    w.append(a)

for i in range(15):
    for j in range(5):
        if i < len(w[j]):
            print(len(w[j]))
            print(w[j][i], end="")
#00 10 20 30 40 01 11 21  