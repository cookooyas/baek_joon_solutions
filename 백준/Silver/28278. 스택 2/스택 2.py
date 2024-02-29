import sys
def commands(n,l,x=0):
    if n==1:
        l.append(x)
    elif n==2:
        if len(l)==0:
            print(-1)
        else:
            print(l.pop())
    elif n==3:
        print(len(l))
    elif n==4:
        print(1 if len(l)==0 else 0)
    elif n==5:
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
            
l=[]
for _ in range(int(sys.stdin.readline())):
    s=sys.stdin.readline()
    if s.startswith("1"):
        n,x=map(int,s.split())
        commands(n,l,x)
    else:
        commands(int(s),l)