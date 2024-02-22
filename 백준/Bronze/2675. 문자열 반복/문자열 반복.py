import sys
for _ in range(int(sys.stdin.readline())):
    n,s=sys.stdin.readline().split()
    new_s=""
    for w in s:
        new_s+=w*int(n)
    print(new_s)