import sys
n=int(sys.stdin.readline())
cnt=0
s=set()
for i in range(n):
    a,b=sys.stdin.readline().split()
    if a=='ChongChong'or b=='ChongChong':
        s.add(a)
        s.add(b)
    if (a in s)or(b in s):
        s.add(a)
        s.add(b)
print(len(s))