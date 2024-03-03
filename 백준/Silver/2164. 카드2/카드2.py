import sys
from collections import deque
l=deque(list(range(1,int(sys.stdin.readline())+1)))

while len(l)>1:
    l.popleft()
    if len(l)==1:
        break;
    tmp=l.popleft()
    l.append(tmp)
print(l[0])