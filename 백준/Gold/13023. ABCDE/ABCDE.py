# 백준 13023 ABCDE

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    global arrive
    visited[v] = True
    if depth == 4:
        arrive = True
        return
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[v] = False

for i in range(n):
    dfs(i, 0)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

