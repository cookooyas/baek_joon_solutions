import sys
max_num,max_idx=0,0
for i in range(9):
    x=int(sys.stdin.readline())
    if x>max_num:
        max_num=x
        max_idx=i+1
print(max_num)
print(max_idx)