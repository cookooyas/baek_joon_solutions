import sys
A=[[0]*100 for _ in range(100)]
for _ in range(int(sys.stdin.readline())):
    x,y=map(int, sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            A[i][j]+=1
print(100*100-sum(A,[]).count(0))