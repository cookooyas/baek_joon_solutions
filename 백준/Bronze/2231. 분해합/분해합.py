import sys
n=int(sys.stdin.readline())
ans=0
for i in range(n):
    sum=i
    for j in str(i):
        sum+=int(j)
    if sum==n:
        ans=i
        break
print(ans)