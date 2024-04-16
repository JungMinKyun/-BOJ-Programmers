# 백준 13305 주유소

import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = 0
n_cost = cost[0]
for i in range(n-1):
    n_cost = min(n_cost, cost[i])
    ans += n_cost * dist[i]

print(ans)