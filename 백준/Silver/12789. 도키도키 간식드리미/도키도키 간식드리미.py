import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
now_num = 1
in_l = []
wait_l = []
indure_cnt=n
while 1:
    indure_cnt += 1
    if len(l) > 0 and l[0] == now_num:
        now_num += 1
        in_l.append(l.pop(0))
        indure_cnt=0
    elif len(wait_l) > 0 and wait_l[0] == now_num:
        now_num += 1
        in_l.append(wait_l.pop(0))
        indure_cnt=0
    elif len(l) > 0 and l[0] != now_num:
        wait_l = [l.pop(0)] + wait_l
        indure_cnt=0
    elif len(l) == 0 and len(wait_l) == 0 and len(in_l) == n:
        print('Nice')
        break
    elif indure_cnt==n:
        print('Sad')
        break