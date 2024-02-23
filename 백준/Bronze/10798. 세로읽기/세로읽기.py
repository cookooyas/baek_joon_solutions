import sys
A=[]
max_len=0
for _ in range(5):
    s=sys.stdin.readline().rstrip()
    if len(s)>max_len:
        max_len=len(s)
    A.append(s)
for i in range(5):
    if len(A[i])<max_len:
        A[i]+=' '*(max_len-len(A[i]))
print("".join([A[j][i]for i in range(max_len) for j in range(5)]).replace(" ",""))