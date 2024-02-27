import sys
ans=666
cnt=1
n=int(sys.stdin.readline())
while 1:
    if cnt==n:
        print(ans)
        break
    ans+=1
    if "666" in str(ans):
        cnt+=1