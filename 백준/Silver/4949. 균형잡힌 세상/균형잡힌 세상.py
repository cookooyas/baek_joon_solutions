import sys
while 1:
    s=sys.stdin.readline().rstrip()
    if s=='.':
        break
    new_s=''
    for w in s:
        if w in '()[]':
            new_s+=w
    for i in range(len(new_s)//2+1):
        new_s=new_s.replace('()','')
        new_s=new_s.replace('[]','')
    print('no' if len(new_s) else 'yes')