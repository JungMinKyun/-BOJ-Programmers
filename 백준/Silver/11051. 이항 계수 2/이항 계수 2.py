# 백준 11051 이항 계수 2

import sys
input = sys.stdin.readline

mod = 10007

n, k = map(int, input().split())

dp = [[1] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod

print(dp[n-k][k])

