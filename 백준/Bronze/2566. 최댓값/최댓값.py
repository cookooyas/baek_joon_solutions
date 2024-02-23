import sys
A=[]
for _ in range(9):
    A.append(list(map(int,sys.stdin.readline().split())))
A=sum(A,[])
max_A=max(A)
print(max_A)
idx=A.index(max_A)
print(idx//9+1,idx%9+1)