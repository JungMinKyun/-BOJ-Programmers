# 백준 1699 제곱수의 합

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for sqt in range(1, i+1):
        square = sqt * sqt
        if square > i:
            break
        
        if dp[i] > dp[i-square] + 1:
            dp[i] = dp[i-square] + 1
        # dp[i] = min(dp[i], dp[i-square]+1)

print(dp[n])