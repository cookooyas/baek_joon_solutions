import sys

def cantor(s='-',n=0):
    global cnt
    if cnt<=n:
        return s
    s+=(' '*len(s)+s)
    return cantor(s,n+1)

while 1:
    try:
        cnt=int(sys.stdin.readline())
        print(cantor())
    except:
        break