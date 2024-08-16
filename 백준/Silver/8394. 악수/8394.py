# 백준 8394 악수

n = int(input())

dp = [0, 0, 2, 3]
count = max(n-3, 0)

for _ in range(count):
    dp.append((dp[-1]+dp[-2])%10)

print(dp[n])