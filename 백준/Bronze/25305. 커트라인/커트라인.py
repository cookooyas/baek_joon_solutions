import sys
n,cut_line=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
l.sort(reverse=True)
print(l[cut_line-1])