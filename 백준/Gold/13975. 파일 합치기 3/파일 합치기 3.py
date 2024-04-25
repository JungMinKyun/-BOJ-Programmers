# 백준 13975 파일 합치기3

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    chapters = list(map(int, input().split()))
    heapq.heapify(chapters)

    result = 0
    while len(chapters) > 1:
        a = heapq.heappop(chapters)
        b = heapq.heappop(chapters)
        result += a+b
        heapq.heappush(chapters, a+b)

    print(result)