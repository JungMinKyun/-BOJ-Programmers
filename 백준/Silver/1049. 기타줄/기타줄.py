# 백준 1049 기타줄

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost = [1000, 1000]
for i in range(m):
    a, b = map(int, input().split())
    cost[0] = min(cost[0], a)
    cost[1] = min(cost[1], b)

print(min(cost[0] * (n//6+1), cost[1] * n, cost[0] * (n//6) + cost[1] * (n%6)))