import sys
n,m=map(int, sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (l[i]+l[j]+l[k])<=m and ans<(l[i]+l[j]+l[k]):
                ans=(l[i]+l[j]+l[k])
print(ans)