# 백준 2346 풍선 터뜨리기

import sys
input = sys.stdin.readline

n = int(input())
balloons = list(map(int, input().split()))
nums = [i for i in range(1, n+1)]
res = []
idx = 0
while len(balloons) >= 2:
    key = balloons.pop(idx)
    value = nums.pop(idx)
    res.append(value)

    if key > 0:
        idx += key-1
        idx %= len(nums)
    else:
        idx += key
        idx %= len(nums)
    
res.append(nums.pop(0))
print(*res)
