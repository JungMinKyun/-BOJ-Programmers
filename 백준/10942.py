# 백준 10942 팰린드롬?

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1 and nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n-i):
        if nums[j] == nums[j+i] and dp[j+1][j+i-1] != 0:
            dp[j][j+i] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])