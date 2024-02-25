import sys
x,n=map(int, sys.stdin.readline().split())
l=[]
for i in range(1,x+1):
    if x%i==0:
        l.append(i)
if n>len(l):
    print(0)
else:
    print(l[n-1])