import sys
n=int(sys.stdin.readline())
if n==0:
    print(1)
else:
    ans=1
    while 1:
        if n==1:
            break
        ans*=n
        n-=1
    print(ans)