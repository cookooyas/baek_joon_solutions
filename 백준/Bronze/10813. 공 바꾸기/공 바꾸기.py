import sys
n,m=map(int,sys.stdin.readline().split())
l=list(range(1,n+1))
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    tmp=l[a-1]
    l[a-1]=l[b-1]
    l[b-1]=tmp
print(*l)