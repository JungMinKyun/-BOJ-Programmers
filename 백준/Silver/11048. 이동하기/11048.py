# 백준 11048 이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

res = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            res[i][j] = board[i][j]
        elif i == 0:
            res[i][j] = board[i][j] + res[i][j-1]
        elif j == 0:
            res[i][j] = board[i][j] + res[i-1][j]
        else:
            res[i][j] = board[i][j] + max(res[i-1][j-1], res[i-1][j], res[i][j-1])

print(res[n-1][m-1])