# 백준 2193 이친수

n = int(input())
dp = [[0, 0] for _ in range(90)]
dp[0] = [0, 1]
dp[1] = [1, 0]

for i in range(2, 90):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]

print(sum(dp[n-1]))