import sys
d={}
for _ in range(int(sys.stdin.readline())):
    name,inout=sys.stdin.readline().split()
    if inout=="enter":
        d[name]=1
    else:
        del d[name]
l=list(d.keys())
l.sort(reverse=True)
print(*l,sep='\n')