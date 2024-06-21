# 백준 9625 BABBA

dp = [0, 1, 1]
for i in range(45):
    dp.append(dp[-1] + dp[-2])

n = int(input())

print(dp[n-1], dp[n])