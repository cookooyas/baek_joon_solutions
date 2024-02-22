import sys
s=sys.stdin.readline().rstrip()
if len(s)%2==0:
    print(int("".join(s[:int(len(s)/2)])=="".join(s[-1:int(len(s)/2-1):-1])))
else:
    print(int("".join(s[:int(len(s)/2)])=="".join(s[-1:int(len(s)/2):-1])))