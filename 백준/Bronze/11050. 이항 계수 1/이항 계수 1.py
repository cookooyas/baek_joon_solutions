import sys
def factorial(n):
    sum=1
    if n!=0:
        for i in range(1,n+1):
            sum*=i
    return sum
n,k=map(int,sys.stdin.readline().split())
print(factorial(n)//factorial(k)//factorial(n-k))