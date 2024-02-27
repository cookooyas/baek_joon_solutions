import sys
s=sys.stdin.readline().rstrip()
l=[]
for w in s:
    l.append(int(w))
l.sort(reverse=True)
print("".join(str(i) for i in l))