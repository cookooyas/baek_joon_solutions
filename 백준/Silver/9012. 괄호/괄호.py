import sys
for _ in range(int(sys.stdin.readline())):
    cnt=0
    for s in sys.stdin.readline().rstrip():
        if s=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            break
    if cnt!=0:
        print('NO')
    else:
        print("YES")