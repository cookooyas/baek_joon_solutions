import sys
while 1:
    x,y,z=map(int, sys.stdin.readline().split())
    l=[x,y,z]
    l.sort()
    if sum(l)==0:
        break
    if l[2]>=(l[0]+l[1]):
        print("Invalid")
    elif l[1]==l[0] and l[1]==l[2]:
        print("Equilateral")
    elif l[1]==l[0] or l[1]==l[2]:
        print("Isosceles")
    else:
        print("Scalene")