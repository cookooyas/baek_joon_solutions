import sys
l=[str(i) for i in range(10)]+[chr(i) for i in range(ord('A'),ord('Z')+1)]
N,B=map(int,sys.stdin.readline().split())
mod=[]
while 1:
    if N>=B:
        mod.append(N%B)
        N=N//B
    else:
        mod.append(N)
        break
print("".join([l[i] for i in reversed(mod)]))