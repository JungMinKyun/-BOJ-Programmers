# 백준 13699 점화식 

dp = [1, 1]

for _ in range(34):
    elt = 0
    for i in range(len(dp)):
        elt += dp[i] * dp[len(dp)-i-1]
    dp.append(elt)

print(dp[int(input())])
