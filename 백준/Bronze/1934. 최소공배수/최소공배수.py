import sys
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
for i in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    print(a*b//gcd(a,b))