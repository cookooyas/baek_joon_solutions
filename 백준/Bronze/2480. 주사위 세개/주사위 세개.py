import sys
[a,b,c]=sorted(list(map(int,sys.stdin.readline().split())))
if a==b and b==c:
    print(10000+a*1000)
elif (a==b)or(b==c):
    print(1000+100*b)
else:
    print(c*100)