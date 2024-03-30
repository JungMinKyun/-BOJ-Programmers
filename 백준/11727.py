# 백준 11727 2xn 타일링 2

n = int(input())

dp = [1, 3]
for i in range(max(1, n)):
    dp.append((dp[-1] + dp[-2]*2)%10007)

print(dp[n-1])