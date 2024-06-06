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


# if n > 1 and m > 1:
#     for i in range(1, n):
#         for j in range(1, m):
#             if dp[i][j] == 1:
#                 ans = max(ans, 1)
#             if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1] and dp[i-1][j-1]+1 == dp[i][j]:
#                 ans = max(ans, dp[i][j])
            
# elif n == 1:
#     ans = max(dp[0])
# elif m == 1:
#     for i in range(n):
#         ans = max(dp[i][0], ans) 
# else:
#     ans = dp[0][0]

# print(ans ** 2)