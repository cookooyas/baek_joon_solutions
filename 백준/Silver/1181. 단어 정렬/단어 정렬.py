import sys
l=[]
for _ in range(int(sys.stdin.readline())):
    l.append(sys.stdin.readline().rstrip())
l=list(set(l))
l.sort(key=lambda x:(len(x),[ord(x[i]) for i in range(len(x))]))
for i in l:
    print(i)