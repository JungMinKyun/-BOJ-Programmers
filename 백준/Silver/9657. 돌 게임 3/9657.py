# 백준 9657 돌 게임 3

n = int(input())
dp = [0, 0, 1, 0 ,0]
for i in range(5, n+1):
    if dp[i-1] == dp[i-3] == dp[i-4] == 0:
        dp.append(1)
    else:
        dp.append(0)

print('CY') if dp[n] else print('SK')