import sys
n,m=map(int,sys.stdin.readline().split())
l=[0]

def dfs(l):
    if len(l)==m+1:
        print(*l[1:])
        return
    for i in range(n):
        if i+1 in l or (i+1)<l[-1]:
            continue
        dfs(l+[i+1])
dfs(l)