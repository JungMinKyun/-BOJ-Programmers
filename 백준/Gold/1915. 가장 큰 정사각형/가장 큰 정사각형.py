# 백준 1915 가장 큰 정사각형

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 :
            dp[i][j] = int(board[i][j])
        elif board[i][j] == '0':
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        ans = max(ans, dp[i][j])

print(ans ** 2)