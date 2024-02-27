import sys
l=[]
for i in range(int(sys.stdin.readline())):
    l.append(list(sys.stdin.readline().split())+[i])
l.sort(key=lambda x : (int(x[0]),x[2]))
for i in l:
    print(*i[0:2])