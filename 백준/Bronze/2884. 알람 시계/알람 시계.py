import sys
h,m=map(int,sys.stdin.readline().split())
if m>=45:
    print(h,m-45)
else:
    if h>0:
        print(h-1,m+15)
    else:
        print(23,m+15)