# 백준 2847 게임을 만든 동준이

import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

result = 0
for i in range(n-1, 0, -1):
    if scores[i] <= scores[i-1]:
        result += scores[i-1] - scores[i] + 1
        scores[i-1] = scores[i] - 1

print(result)