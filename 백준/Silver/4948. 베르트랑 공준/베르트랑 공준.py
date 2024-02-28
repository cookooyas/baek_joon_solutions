import sys

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

l=[False]+[is_prime(i) for i in range(2,123456*2+1)]
while 1:
    n=int(sys.stdin.readline())
    if n==0:
        break
    print(sum(l[n:2*n]))