import sys
n,m=map(int,sys.stdin.readline().split())
l=[]
cnt=0
for _ in range(n):
    l.append(sys.stdin.readline().rstrip())
for _ in range(m):
    s=sys.stdin.readline().rstrip()
    if s in l:
        cnt+=1
print(cnt)