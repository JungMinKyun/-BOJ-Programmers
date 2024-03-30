# 백준 15990 1, 2, 3 더하기 5

import sys
input = sys.stdin.readline

mod = 1e9 + 9

dp = [[0, 0, 0] for _ in range(100000)]
dp[0] = [1, 0 ,0]
dp[1] = [0, 1, 0]
dp[2] = [1, 1, 1]
for i in range(3, 100000):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % mod
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % mod

for _ in range(int(input())):
    print(int(sum(dp[int(input())-1]) % mod))
