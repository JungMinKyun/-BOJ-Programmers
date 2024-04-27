# 백준 21758 꿀 따기

import sys
input = sys.stdin.readline
n = int(input())
honey = list(map(int, input().split()))
res = 0

cum_sum = [0] * n
cum_sum[0] = honey[0]
for i in range(1, n):
    cum_sum[i] = cum_sum[i-1] + honey[i]

for i in range(1, n-1):
    res = max(res, 2*cum_sum[n-1] - honey[0] - honey[i] - cum_sum[i])

for i in range(1, n-1):
    res = max(res, cum_sum[n-2] + cum_sum[i-1] - honey[i])

for i in range(1, n-1):
    res = max(res, honey[i] + cum_sum[n-2] - honey[0])

print(res)