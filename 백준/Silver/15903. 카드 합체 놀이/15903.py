# 백준 15903 카드 합체 놀이

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(m):
    temp = 0
    for i in range(2):
        temp += heapq.heappop(cards)
    for i in range(2):
        heapq.heappush(cards, temp)

print(sum(cards))