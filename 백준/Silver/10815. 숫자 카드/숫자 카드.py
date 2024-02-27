import sys
d={}
_ = sys.stdin.readline()
l1 = list(map(int,sys.stdin.readline().split()))
m = sys.stdin.readline()
l2 = list(map(int,sys.stdin.readline().split()))
for i in l2:
    d[i]=0
for i in l1:
    if i in d:
        d[i]+=1
print(*d.values())
    