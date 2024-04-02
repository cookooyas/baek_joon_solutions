import sys
n,k=map(int, sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
sum_l=[sum(l[:k])]
for i in range(n-k):
    sum_l.append(sum_l[i]-l[i]+l[i+k])
print(max(sum_l))