import sys
n,m=map(int,sys.stdin.readline().split())
d={}
for i in range(n):
    d[sys.stdin.readline().rstrip()]=i+1
l=list(d.keys())
for i in range(m):
    s=sys.stdin.readline().rstrip()
    if s.isdigit():
        print(l[int(s)-1])
    else:
        print(d[s])