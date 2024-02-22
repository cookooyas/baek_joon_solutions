import sys
s=sys.stdin.readline().rstrip().upper()
s_dict={}
for i in s:
    if not i in s_dict:
        s_dict[i]=1
    else:
        s_dict[i]+=1
max_cnt=0
max_s=""
for k,v in s_dict.items():
    if v>max_cnt:
        max_s=k
        max_cnt=v
    elif v==max_cnt:
        max_s="?"
print(max_s)