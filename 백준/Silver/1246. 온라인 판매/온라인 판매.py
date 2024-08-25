# 백준 1246 온라인 판매

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(m)]
nums.sort()

res = 0 
target = 0 
for i in range(m):
    egg = min(m - i, n) 

    if res < nums[i] * egg:
        res = nums[i] * egg 
        target = nums[i] 

print(target, res)