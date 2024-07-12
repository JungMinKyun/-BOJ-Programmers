# 백준 1940 주몽

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))

nums.sort()
count, left, right = 0, 0, n-1

while left < right:
    temp = nums[left] + nums[right]
    if temp < m: left += 1
    elif temp > m: right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)