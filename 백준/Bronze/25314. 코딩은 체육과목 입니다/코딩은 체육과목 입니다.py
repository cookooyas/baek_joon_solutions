import sys,math
n=int(sys.stdin.readline())
s=""
for _ in range(math.ceil(n/4)):
    s+="long "
print(s+"int")