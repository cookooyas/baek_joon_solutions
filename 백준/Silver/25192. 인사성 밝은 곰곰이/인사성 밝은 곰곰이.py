import sys
d=set()
cnt=0
for _ in range(int(sys.stdin.readline())):
    s=sys.stdin.readline().rstrip()
    if s=='ENTER':
        d=set()
    else:
        if s not in d:
            d.add(s)
            cnt+=1
print(cnt)