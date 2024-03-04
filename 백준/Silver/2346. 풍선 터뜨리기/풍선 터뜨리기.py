import sys
n=int(sys.stdin.readline())
nl=list(map(int,sys.stdin.readline().split()))
l=[[i+1,nl[i]] for i in range(n)]
ans=[]
idx=0
while len(l)>0:
    # print('현재l:',l)
    [cnt,num]=l.pop(0)
    # print(cnt,'번 공 추출,',num,"만큼 이동해야함.")
    ans.append(cnt)
    num=num-1 if num>0 else num
    if abs(num)>len(l) and len(l)>0:
        if num>0:
            num=num%len(l)
        else:
            num=-abs(num)%len(l)
    elif len(l)==0:
        break
    # print("실제로 이동해야하는 좌표:",num)
    l=l[num:]+l[:num]
    # print('변경된 l :',l)
    # print(ans)
    # print('*'*100)
print(*ans)