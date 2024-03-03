import sys
from collections import deque
def commands(c,l,x="0"):
    if c=='push':
        l.append(x)
    elif c=='pop':
        if len(l)>0:
            print(l.popleft())
        else:
            print(-1)
    elif c=='size':
        print(len(l))
    elif c=='empty':
        print(1 if len(l)==0 else 0)
    elif c=='front':
        if len(l)>0:
            print(l[0])
        else:
            print(-1)
    elif c=='back':
        if len(l)>0:
            print(l[-1])
        else:
            print(-1)
l=deque()
for _ in range(int(sys.stdin.readline())):
    c=sys.stdin.readline().rstrip()
    if c.startswith('push'):
        c,x=c.split()
        commands(c,l,x=x)
    else:
        commands(c,l)