import sys
a,b,c=map(int, sys.stdin.readline().split())
l=[a,b,c]
l.sort()
if l[2]>=(l[0]+l[1]):
    print(2*(l[0]+l[1])-1)
else:
    print(sum(l))