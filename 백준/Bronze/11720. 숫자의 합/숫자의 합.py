import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip()
sum=0
for w in s:
    sum+=int(w)
print(sum)