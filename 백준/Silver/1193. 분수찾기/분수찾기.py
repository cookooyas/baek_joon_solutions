import sys
n=int(sys.stdin.readline())
line_num=1
cnt=1
while 1:
    if line_num>=n:
        break
    cnt+=1
    line_num += cnt
if cnt%2==0:
    ans=str(cnt-(line_num-n)%cnt)+"/"+str((line_num-n)%cnt+1)
else:
    ans=str((line_num-n)%cnt+1)+"/"+str(cnt-(line_num-n)%cnt)
print(ans)