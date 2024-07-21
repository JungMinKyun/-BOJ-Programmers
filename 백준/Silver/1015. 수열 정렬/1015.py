# 백준 1015 수열 정렬

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = [0] * n
ans = [0] * n
sorted_nums = sorted(nums)

for i in range(n):
    num = sorted_nums[i]

    for j in range(n):
        if nums[j] == num and visited[j] == 0:
            visited[j] = 1
            ans[j] = i
            break

print(*ans)