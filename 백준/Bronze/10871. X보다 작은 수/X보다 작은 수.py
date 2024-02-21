import sys
_,N=map(int,sys.stdin.readline().split())
s=""
for i in list(map(int,sys.stdin.readline().split())):
    if i<N:
        s+=str(i)+" "
print(s)