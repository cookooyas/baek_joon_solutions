import sys
normal=[1,1,2,2,2,8]
cnt=0
ans=[]
for i in map(int,sys.stdin.readline().split()):
    ans.append(normal[cnt]-i)
    cnt+=1
print(*ans)