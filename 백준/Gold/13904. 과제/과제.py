# 백준 13904 과제

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hw = []
max_day = 0
for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hw, (-w, d))
    max_day = max(max_day, d)

days = [0] * (max_day+1)

while hw:
    w, d = heapq.heappop(hw)
    w *= -1
    for i in range(d, 0, -1):
        if not days[i]:
            days[i] = w
            break
print(sum(days))