# 백준 1138 한 줄로 서기

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n

for height in range(n):
    posit = nums[height]
    height += 1

    for i in range(n):
        if posit == 0 and ans[i] == 0:
            ans[i] = height
            break
        if ans[i] == 0:
            posit -= 1

print(*ans)