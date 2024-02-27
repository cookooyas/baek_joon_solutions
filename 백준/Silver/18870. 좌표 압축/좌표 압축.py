import sys
N=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
s_l=list(set(l))
s_l.sort()
d={}
ans=[]
for i in range(len(s_l)):
    d[s_l[i]]=i
for i in l:
    ans.append(d[i])
print(*ans)