# 백준 1107 리모컨

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bugs = list(map(str, input().split()))
cnt = abs(n - 100)

for nums in range(1000001):
    for i in range(len(str(nums))):
        if str(nums)[i] in bugs:
            break
        elif i == len(str(nums)) - 1:
            cnt = min(cnt, abs(nums - n) + len(str(nums)))
print(cnt)