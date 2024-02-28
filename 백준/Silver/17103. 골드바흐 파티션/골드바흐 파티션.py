import sys

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [False,False]+sieve[2:]

l=prime_list(1000000)

for _ in range(int(sys.stdin.readline())):
    cnt=0
    n=int(sys.stdin.readline())
    for i in range(2,n//2+1):
        if l[n-i] and l[i]:
            cnt+=1
    print(cnt)