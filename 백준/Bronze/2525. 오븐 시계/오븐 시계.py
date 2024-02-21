import sys
h,m=map(int,sys.stdin.readline().split())
x=int(sys.stdin.readline())

print((h+(x+m)//60)%24,(x+m)%60)