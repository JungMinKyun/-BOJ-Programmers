# 백준 1434 책 정리

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if boxes[i] >= books[j]:
            boxes[i] -= books[j]
            books[j] = 0
        else:
            books[j] -= boxes[i]
            boxes[i] = 0

print(sum(boxes))