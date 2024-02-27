import sys
real_chess=[sum([[1,0,1,0,1,0,1,0] if i%2==0 else [0,1,0,1,0,1,0,1] for i in range(8)],[]),sum([[1,0,1,0,1,0,1,0] if i%2==1 else [0,1,0,1,0,1,0,1] for i in range(8)],[])]
board = []
min_square = 100
cnt=0
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    board.append(sys.stdin.readline().rstrip().replace("W","0").replace("B","1"))

for i in range(n - 7):
    for j in range(m - 7):
        chess = sum([[int(x) for x in board[y][j:j + 8]] for y in range(i,i + 8)],[])
        for a in range(2):
            cnt=sum([x!=y for x,y in zip(chess,real_chess[a])])
            if min_square>cnt:
                min_square=cnt
print(min_square)