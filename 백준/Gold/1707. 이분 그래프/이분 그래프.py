# 백준 1707 이분 그래프

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v+1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    trigger = False
    def dfs(v, visited, sign):
        global trigger
        for k in graph[v]:
            if visited[k] == 0:
                visited[k] = -sign
                dfs(k, visited, -sign)
            elif visited[k] == sign:
                trigger = True
                return 
        
    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, visited, 1)

    if trigger:
        print('NO')
    else:
        print('YES')