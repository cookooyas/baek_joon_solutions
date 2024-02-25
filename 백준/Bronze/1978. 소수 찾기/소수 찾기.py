import sys
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
ans=0
for i in l:
    if i!=1:
        cnt=0
        for j in range(2,i+1):
            if i%j==0:
                cnt+=1
        if cnt==1:
            ans+=1
print(ans)