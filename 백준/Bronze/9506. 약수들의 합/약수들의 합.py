import sys
while 1:
    n=int(sys.stdin.readline())
    l=[]
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if(sum(l)==n):
        print(str(n)+" = "+" + ".join(map(str,l)))
    else:
        print(str(n)+" is NOT perfect.")