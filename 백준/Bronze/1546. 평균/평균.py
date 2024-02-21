import sys
_=int(sys.stdin.readline())
l= list(map(int,sys.stdin.readline().split()))
max_score=max(l)
sum=0
for i in l:
    sum+=i/max_score*100
print(sum/len(l))