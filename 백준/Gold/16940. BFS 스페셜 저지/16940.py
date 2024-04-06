# 백준 16940 BFS 스페셜 저지

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

query = list(map(int, input().split()))
if query[0] == 1:
    visited = [False] * (n+1)
    parch = [-1] * (n+1)

    for i in range(n):
        parch[query[i]] = i+1

    for i in range(n):
        graph[i+1] = sorted(graph[i+1], key=lambda x : parch[x])

    Q = deque()
    Q.append(query[0])
    visited[query[0]] = True
    ans = []
    while Q:
        x = Q.popleft()
        ans.append(x)
        for k in graph[x]:
            if not visited[k]:
                Q.append(k)
                visited[k] = True

    if ans == query:
        print(1)
    else:
        print(0)

else:
    print(0)