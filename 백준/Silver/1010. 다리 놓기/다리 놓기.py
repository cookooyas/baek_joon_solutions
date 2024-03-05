import sys
def factorial(n):
    sum=1
    if n>1:
        for i in range(1,n+1):
            sum*=i
    return sum
for _ in range(int(sys.stdin.readline())):
    n,m=map(int,sys.stdin.readline().split())
    print(factorial(m)//factorial(n)//factorial(m-n))