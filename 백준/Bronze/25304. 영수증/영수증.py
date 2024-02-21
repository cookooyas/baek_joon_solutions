import sys
sum=0
total_price=int(sys.stdin.readline())
N=int(sys.stdin.readline())
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    sum+=a*b
print("Yes") if sum==total_price else print("No")