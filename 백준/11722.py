# 백준 11722 가장 긴 감소하는 부분 수열

N = int(input())
array = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = min(dp[i], dp[j]-1)

print(-min(dp)+1)