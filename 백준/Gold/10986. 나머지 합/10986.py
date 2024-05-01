# 백준 10986 나머지 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
cum_sum = [0] * n
remainders = [0] * m

cum_sum[0] = nums[0]
remainders[cum_sum[0] % m] += 1

for i in range(1, n):
    cum_sum[i] = cum_sum[i-1] + nums[i]
    remainders[cum_sum[i] % m] += 1

ans += remainders[0]
for i in range(m):
    ans += remainders[i] * (remainders[i] - 1) // 2
print(ans)