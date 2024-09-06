# 백준 1236 성 지키기

n, m = map(int, input().split())
board = [str(input()) for _ in range(n)]

rc, cc = 0, 0
for i in range(n):
    if 'X' not in board[i]:
        rc += 1

for j in range(m):
    flag = False
    for i in range(n):
        if board[i][j] == 'X':
            flag = True
    if not flag:
        cc += 1

print(max(rc, cc))