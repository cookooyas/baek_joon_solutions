import sys
l=list(range(1,31))
while 1:
    try:
        idx = int(sys.stdin.readline())
        l[idx - 1] = 0
    except:
        break
print(*[i for i in l if i!=0 ])