import sys
n,m=map(int,sys.stdin.readline().split())
l=[]

def dfs(l):
    if len(l)==m:
        print(*l)
        return
    for i in range(n):
        if i+1 in l:
            continue
        dfs(l+[i+1])
dfs(l)