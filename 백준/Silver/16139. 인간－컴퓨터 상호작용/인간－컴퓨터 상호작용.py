import sys
word=sys.stdin.readline().rstrip()
n=int(sys.stdin.readline())

for _ in range(n):
    s,l,k=sys.stdin.readline().split()
    l,k=int(l),int(k)
    length=k-l+1
    print(length-len("".join(word[l:k+1]).replace(s,'')))