import sys
sum=0
for _ in range(int(sys.stdin.readline())):
    last_s=[""]
    w=sys.stdin.readline().rstrip()
    for s in w:
        if (s!=last_s[-1]) and (s in last_s):
            sum-=1
            break
        last_s.append(s)
    sum+=1
print(sum)