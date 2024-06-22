#  백준 13301 타일 장식물

dp = [1, 1]
for i in range(80):
    dp.append(dp[-1] + dp[-2])

n = int(input())
print(2*(dp[n]+dp[n-1]))