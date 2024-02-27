import sys
l=[0]*10000
for _ in range(int(sys.stdin.readline())):
    l[int(sys.stdin.readline())-1]+=1
for i in range(10000):
    if l[i]!=0:
        for j in range(l[i]):
            print(i+1)
