import sys
a,b=map(int,sys.stdin.readline().split())
c=int(sys.stdin.readline())
n0=int(sys.stdin.readline())
if b>0:
    if (c-a)<0:
        if n0<=b/(c-a):
            print(1)
        else:
            print(0)
    elif (c-a)==0:
        if b==0:
            print(1)
        else:
            print(0)
    else:
        if n0>=b/(c-a):
            print(1)
        else:
            print(0)
else:
    if(c-a)<0:
        print(0)
    else:
        print(1)