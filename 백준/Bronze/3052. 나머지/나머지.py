import sys
d={}
for _ in range(10):
    x=int(sys.stdin.readline())
    d[x%42]=1
print(len(d))