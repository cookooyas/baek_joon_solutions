import sys
l=[str(i) for i in range(10)]+[chr(i) for i in range(ord('A'),ord('Z')+1)]
N,B=sys.stdin.readline().split()
ans=0
cnt=len(N)-1
for w in N:
    ans+=int(B)**cnt*l.index(w)
    cnt-=1
print(ans)