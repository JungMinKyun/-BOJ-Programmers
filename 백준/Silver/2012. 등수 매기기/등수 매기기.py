# 백준 2012 등수 매기기

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

ans = 0
for i in range(n):
    ans += abs(nums[i] - (i+1))

print(ans)