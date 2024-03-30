# 백준 1715번 카드 정렬하기

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for i in range(n):
    heapq.heappush(hq, int(input()))

ans = 0
while len(hq) >  1:
    temp = 0
    for _ in range(2):
        temp += heapq.heappop(hq)
    ans += temp
    heapq.heappush(hq, temp)

print(ans)