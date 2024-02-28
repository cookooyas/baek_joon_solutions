import sys
n,m=map(int, sys.stdin.readline().split())
d={}
for _ in range(n+m):
    s=sys.stdin.readline().rstrip()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
l=[k for k,v in d.items() if v==2]
l.sort()
print(len(l))
print(*l,sep='\n')