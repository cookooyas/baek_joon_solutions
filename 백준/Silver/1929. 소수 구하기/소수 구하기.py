import sys
def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

n,m=map(int,sys.stdin.readline().split())

for i in range(n,m+1):
    if i!=1 and is_prime(i):
        print(i)