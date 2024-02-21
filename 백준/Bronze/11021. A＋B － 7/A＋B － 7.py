import sys
N=int(sys.stdin.readline())
for i in range(N):
    print("Case #"+str(i+1)+":"+" "+str(sum(map(int,sys.stdin.readline().split()))))