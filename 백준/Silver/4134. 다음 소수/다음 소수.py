import sys
def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    while 1:
        if n==0 or n==1:
            print(2)
            break
        if is_prime(n):
            print(n)
            break
        n+=1