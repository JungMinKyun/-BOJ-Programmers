# 백준 2468 안전영역

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

high = 0
for i in range(n):
    high = max(max(board[i]), high)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, level):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>level and visited[nx][ny]==0:
                visited[nx][ny] = 1
                Q.append((nx, ny))

ans = 0
for level in range(high):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]>level and visited[i][j]==0:
                bfs(i ,j, level)
                count += 1
    ans = max(ans, count)

print(ans)