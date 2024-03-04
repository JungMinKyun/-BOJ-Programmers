# 백준 11000번 강의실 배정

import heapq
import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key = lambda x: (x[0], x[1]))

heap = []
heapq.heappush(heap, times[0][1])

for i in range(1, n):
    if heap[0] <= times[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, times[i][1])

print(len(heap))