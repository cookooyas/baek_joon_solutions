import sys
n=2
for _ in range(int(sys.stdin.readline())):
    n+=(n-1)
print(n**2)