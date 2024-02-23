import sys
n,m=map(int,sys.stdin.readline().split())
A=[]
B=[]
for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))
for _ in range(n):
    B.append(list(map(int,sys.stdin.readline().split())))
A=sum(A,[])
B=sum(B,[])
ans=[A[i]+B[i] for i in range(n*m)]
for i in range(n):
    print(*ans[m*i:m*(i+1)])