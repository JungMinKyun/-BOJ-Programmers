# 백준 9465 스티커

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]

    if n > 1:
        dp[0][1] = array[0][1] + array[1][0]    
        dp[1][1] = array[1][1] + array[0][0]

    for i in range(2, n):
        dp[0][i] = array[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = array[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
