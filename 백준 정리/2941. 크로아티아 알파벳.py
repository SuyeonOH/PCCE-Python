import sys
word=sys.stdin.readline().rstrip()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    word=word.replace(i,'*')
print(len(word))