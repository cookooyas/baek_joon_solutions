import sys
x,y=sys.stdin.readline().split()
print(max(int("".join(reversed(x))),int("".join(reversed(y)))))