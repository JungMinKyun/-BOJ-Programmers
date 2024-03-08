# 백준 1202번 보석 도둑

import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewerlys = [list(map(int, input().split())) for _ in range(n)]
bags = []
for _ in range(k):
    bags.append(int(input()))

jewerlys.sort()
bags.sort()

result = 0
hq = []

for bag in bags:
    while jewerlys and jewerlys[0][0] <= bag:
        heapq.heappush(hq, -jewerlys[0][1])
        heapq.heappop(jewerlys)
    if hq:
        result -= heapq.heappop(hq)

print(result)