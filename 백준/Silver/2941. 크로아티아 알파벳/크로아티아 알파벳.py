import sys
words=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=sys.stdin.readline().rstrip()
s_dict={}
for w in words:
    if w in s:
        if not w in s_dict:
            s_dict[w]=0
        s_dict[w]+=s.count(w)
s_len=len(s)
if 'dz='in s_dict and 'z='in s_dict:
    s_dict['z=']-=s_dict['dz=']
for k,v in s_dict.items():
    s_len-=len(k)*v
print(sum(s_dict.values())+s_len)