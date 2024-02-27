import sys
n=int(sys.stdin.readline())
ans=-1
for i in range(n//5+1):
    now_n=n-i*5
    if now_n%3==0:
        cnt=i+now_n//3
        if ans==-1 or ans>cnt:
            ans=cnt
print(ans)