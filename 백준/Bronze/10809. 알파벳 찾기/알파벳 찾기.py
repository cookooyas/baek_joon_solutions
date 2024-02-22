import sys
alphabet_list=[chr(i) for i in range(ord('a'),ord('z')+1)]
alphabet_dict={}
for i in alphabet_list:
    alphabet_dict[i]=-1
s=sys.stdin.readline().rstrip()
for i in range(len(s)):
    if alphabet_dict[s[i]]==-1:
        alphabet_dict[s[i]]=i
print(*alphabet_dict.values())