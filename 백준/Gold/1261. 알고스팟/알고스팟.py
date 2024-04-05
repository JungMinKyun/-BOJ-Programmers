# 백준 1261 알고스팟
 
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0 ,-1, 1]

Q = deque()
Q.append((0, 0))
visited[0][0] = 0
while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
            if board[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                Q.appendleft((nx, ny))
            else:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))

print(visited[n-1][m-1])

