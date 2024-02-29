import sys
n=int(sys.stdin.readline())
length=0
cnt=1
while 1:
    length+=cnt*2+1
    if length>=n:
        print(cnt)
        break
    cnt+=1