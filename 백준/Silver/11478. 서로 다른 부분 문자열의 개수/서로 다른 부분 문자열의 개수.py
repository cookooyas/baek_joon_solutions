import sys
s=sys.stdin.readline().rstrip()
l=[]
for i in range(len(s)):
    l+=["".join(s[x:x+1+i]) for x in range(len(s)-i)]
print(len(set(l)))