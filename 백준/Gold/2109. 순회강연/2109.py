# 백준 2109 순회공연

import heapq
import sys
input = sys.stdin.readline

n = int(input())
lectures = []
max_day = 0
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(lectures, (-p, d))
    max_day = max(max_day, d)

days = [0] * (max_day+1)

while lectures:
    p, d = heapq.heappop(lectures)
    p *= -1
    for i in range(d, 0, -1):
        if not days[i]:
            days[i] = p
            break

print(sum(days))