# 백준 15661 링크와 스타트

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
INF = 1e9
res = INF

def dfs():
    global res
    A, B = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                A += board[i][j]
            elif not visited[i] and not visited[j]:
                B += board[i][j]
    res = min(res, abs(A - B))
    return

def solve(idx):
    if idx == n:
        dfs()
        return
    visited[idx] = True
    solve(idx + 1)
    visited[idx] = False
    solve(idx + 1)

solve(0)
print(res)