# 백준 2133 타일 채우기

n = int(input())
dp = [0, 3] + [0] * 14
sum_dp = [0, 3] + [0] * 14

for i in range(2, 16):
    dp[i] = dp[i-1] * 3 + sum_dp[i-2] * 2 + 2
    sum_dp[i] = sum_dp[i-1] + dp[i]

if n % 2 == 0:
    print(dp[n//2])
else:
    print(0)