import sys
from collections import deque, Counter
n=int(sys.stdin.readline())
dq=deque()
for _ in range(n):
    dq.append(int(sys.stdin.readline()))
dq=sorted(dq)
counter=Counter(dq)
v=counter.most_common(2)
print(int(round(sum(dq)/n,0)))
print(dq[n//2])
if len(dq)>1:
    print(v[0][0] if v[0][1]!=v[1][1] else v[1][0])
else:
    print(dq[0])
print(max(dq)-min(dq))