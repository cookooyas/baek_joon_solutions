import sys
l=[]
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    if n!=0:
        l.append(n)
    else:
        l.pop()
print(sum(l))