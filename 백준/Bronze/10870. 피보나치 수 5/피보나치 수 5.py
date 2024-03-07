import sys
n=int(sys.stdin.readline())
cnt=1
n1,n2=0,1
ans=1
while 1:
    if n==0:
        print(0)
        break
    if cnt == n:
        print(ans)
        break
    ans=n2+n1
    n1=n2
    n2=ans
    cnt+=1
