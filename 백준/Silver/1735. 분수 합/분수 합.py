import sys
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())

e,f=a*d+b*c,b*d

gcd_num=gcd(e,f)

print(e//gcd_num,f//gcd_num)