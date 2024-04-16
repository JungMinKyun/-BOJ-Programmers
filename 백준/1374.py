# 백준 1374 강의실

import sys
import heapq
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, input().split())) for _ in range(n)]

rooms.sort(key=lambda x: x[1])

ans = 0
heap = []
for i in range(n):
    while heap and heap[0] <= rooms[i][1]:
        heapq.heappop(heap)
    heapq.heappush(heap, rooms[i][2])
    ans = max(ans, len(heap))

print(ans)