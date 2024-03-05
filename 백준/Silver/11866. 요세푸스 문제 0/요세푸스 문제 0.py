import sys
n,k=map(int,sys.stdin.readline().split())
l=[i for i in range(1,n+1)]
idx=0
ans=[]
while len(l)>0:
    if k<=len(l):
        idx=k-1
        ans.append(str(l.pop(idx)))
    else:
        idx=k%len(l)-1 if k%len(l)>0 else len(l)-k%len(l)-1
        ans.append(str(l.pop(idx)))
    l=l[idx:]+l[:idx]

print("<"+', '.join(ans)+">")