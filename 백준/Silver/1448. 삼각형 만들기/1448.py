# 백준 1448 삼각형 만들기

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

ans = -1
for i in range(n-2):
    if nums[i] < nums[i+1] + nums[i+2]:
        ans = max(ans, nums[i]+nums[i+1]+nums[i+2])

print(ans)