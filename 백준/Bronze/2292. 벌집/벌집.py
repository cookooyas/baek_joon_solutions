import sys
n=int(sys.stdin.readline())
cnt=1
hive=1
while 1:
    if hive >= n:
        break
    else:
        hive+=cnt*6
        cnt+=1
print(cnt)