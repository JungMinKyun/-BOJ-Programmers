# 백준 1398 동전문제

import sys
input = sys.stdin.readline

coins = [1, 10, 25]
dp = [0] + [1e15 + 1] * 99

for c in coins:
    for i in range(c, 100):
        dp[i] = min(dp[i], dp[i-c]+1)

for i in range(int(input())):
    n = int(input())
    ans = 0
    while n:
        ans += dp[n % 100]
        n //= 100
    print(ans)