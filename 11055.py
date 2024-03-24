# 백준 11055 가장 큰 증가하는 부분 수열

N = int(input())
array = list(map(int, input().split()))

dp = [array[0]] + [0] * (N-1)

for i in range(N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+array[i])
        else:
            dp[i] = max(dp[i], array[i])

print(max(dp))