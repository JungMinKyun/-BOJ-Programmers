# 백준 15624 피보나치 수 7

n = int(input())
mod = 1000000007

dp = [0, 1]
for i in range(n-1):
    dp.append((dp[-1] + dp[-2]) % mod)

print(dp[n])