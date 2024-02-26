import sys
x_l=[]
y_l=[]
for _ in range(3):
    x,y=map(int, sys.stdin.readline().split())
    x_l.append(x)
    y_l.append(y)
x_l.sort()
y_l.sort()
ans=[]
if x_l[1]==x_l[0]:
    ans.append(x_l[2])
else:
    ans.append(x_l[0])
if y_l[1]==y_l[0]:
    ans.append(y_l[2])
else:
    ans.append(y_l[0])
print(*ans)