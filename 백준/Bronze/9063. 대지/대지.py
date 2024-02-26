import sys
n=int(sys.stdin.readline())
if n<2:
    print(0)
else:
    x_l=[]
    y_l=[]
    for _ in range(n):
        x,y=map(int, sys.stdin.readline().split())
        x_l.append(x)
        y_l.append(y)
    print((max(x_l)-min(x_l))*(max(y_l)-min(y_l)))