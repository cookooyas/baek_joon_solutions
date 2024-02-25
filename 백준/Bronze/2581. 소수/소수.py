import sys
a,b=int(sys.stdin.readline()),int(sys.stdin.readline())
ans=[]
for i in range(a,b+1):
    cnt=0
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
    if cnt==1:
        ans.append(i)
if len(ans)==0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))