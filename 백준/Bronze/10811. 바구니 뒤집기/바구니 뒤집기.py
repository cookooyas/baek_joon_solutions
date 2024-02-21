import sys
n,m = map(int, sys.stdin.readline().split())
l=list(range(1,n+1))
for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    l[i-1:j]=reversed(l[i-1:j])
print(*l)