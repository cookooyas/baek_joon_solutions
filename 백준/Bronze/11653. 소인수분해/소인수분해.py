import sys
n=int(sys.stdin.readline())
a=2
while n>1:
    if n%a==0:
        print(a)
        n/=a
    else:
        a+=1