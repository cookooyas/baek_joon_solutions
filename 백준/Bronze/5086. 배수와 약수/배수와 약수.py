import sys
while 1:
    x,y=map(int,sys.stdin.readline().split())
    if x==0 and y==0:
        break
    if x%y==0 and x//y>=2:
        print('multiple')
    elif y%x==0 and y//x>=2:
        print('factor')
    else:
        print('neither')