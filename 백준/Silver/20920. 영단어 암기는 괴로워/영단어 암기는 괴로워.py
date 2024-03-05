import sys
n,m=map(int,sys.stdin.readline().split())
d={}
l=[]
for _ in range(n):
    s=sys.stdin.readline().rstrip()
    if len(s)>=m:
        if s not in d:
            d[s]=1
        else:
            d[s]+=1
        l.append(s)
l=list(set(l))
l=sorted(l,key=lambda x : (-d[x],-len(x),x))
print(*l,sep='\n')