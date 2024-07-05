# 백준 1083 소트

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = int(input())

# trial = 1
# while trial <= s:
#     for i in range(n):
#         if nums[i] >= nums[i+1]:
#             continue
#         nums[i], nums[i+1] = nums[i+1], nums[i]
#         trial += 1
#         break

# print(*nums)

for i in range(n):
    if s == 0:
        break
    maxim = max(nums[i:i+s+1])
    maxid = nums.index(maxim)
    while maxid != i and s:
        nums[maxid], nums[maxid-1] = nums[maxid-1], nums[maxid]
        maxid, s = maxid-1, s-1

print(*nums)