import sys
n=int(sys.stdin.readline())
ans=1
while n>0:
    ans*=n
    n-=1
print(ans)