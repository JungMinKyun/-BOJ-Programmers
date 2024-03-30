# 백준 16194 카드 구매하기 2

n = int(input())
cards = list(map(int, input().split()))

dp = [1e9] * (n+1)
dp[1:n+1] = cards

for i in range(n):
    card = cards[i]
    for j in range(i+1, n+1):
        dp[j] = min(dp[j-(i+1)] + card, dp[j])

print(dp[n])