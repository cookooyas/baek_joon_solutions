import sys
from collections import deque

def commands(n,d,x=0):
    if n==1:
        d.appendleft(x)
    elif n==2:
        d.append(x)
    elif n==3:
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
    elif n==4:
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())
    elif n==5:
        print(len(d))
    elif n==6:
        print(0 if len(d)>0 else 1)
    elif n==7:
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    elif n==8:
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])
d=deque()
for _ in range(int(sys.stdin.readline())):
    s=sys.stdin.readline().rstrip()
    if len(s)>1:
        n,x=map(int,s.split())
        commands(n,d,x)
    else:
        commands(int(s),d)