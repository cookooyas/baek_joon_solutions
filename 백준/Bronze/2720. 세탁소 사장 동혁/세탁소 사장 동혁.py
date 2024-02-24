import sys
for _ in range(int(sys.stdin.readline())):
    N=int(sys.stdin.readline())
    change=[]
    change.append(N//25)
    N=N%25
    change.append(N//10)
    N=N%10
    change.append(N//5)
    change.append(N%5)
    print(*change)