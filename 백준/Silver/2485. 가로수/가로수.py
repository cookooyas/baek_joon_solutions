import sys
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

l=[]
for _ in range(int(sys.stdin.readline())):
    l.append(int(sys.stdin.readline()))
l=[l[i+1]-l[i] for i in range(len(l)-1)]

gcd_num=l[0]
for i in range(len(l)-1):
    gcd_num=gcd(l[i+1],gcd_num)
sum=0
for i in l:
    sum+=i//gcd_num-1
print(sum)