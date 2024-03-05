# 큐 fifo 스택 lifo
import sys
from collections import deque
_=int(sys.stdin.readline())
qs_l=list(map(int,sys.stdin.readline().split()))
l=list(map(int,sys.stdin.readline().split()))
_=int(sys.stdin.readline())
quest=list(map(int,sys.stdin.readline().split()))
ans=[]

q_l=deque([l[x] for x in range(len(qs_l)) if qs_l[x]==0])
for i in quest:
    q_l.appendleft(i)
    ans.append(q_l.pop())
print(*ans)