# 백준 3273 두 수의 합

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

start, end, ans = 0, n-1, 0
while start < end:
    if nums[start] + nums[end] == x:
        ans += 1
        start += 1
    elif nums[start] + nums[end] < x:
        start += 1
    elif nums[start] + nums[end] > x:
        end -= 1

print(ans)