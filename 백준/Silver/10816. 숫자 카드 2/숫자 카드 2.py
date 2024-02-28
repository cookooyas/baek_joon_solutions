import sys
_=int(sys.stdin.readline())
l1=list(map(int,sys.stdin.readline().split()))
_=int(sys.stdin.readline())
l2=list(map(int,sys.stdin.readline().split()))
d={}
for i in l2:
    d[i]=0
for i in l1:
    if i in d:
        d[i]+=1
print(*[d[i] for i in l2])