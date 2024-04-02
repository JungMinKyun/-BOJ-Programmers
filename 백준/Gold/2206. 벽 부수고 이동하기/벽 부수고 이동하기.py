# 백준 2206 벽 부수고 이동하기

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    Q = deque()
    Q.append((x, y, z))
    
    while Q:
        x, y, z = Q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                Q.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                Q.append((nx, ny, z))
    
    return -1

ans = bfs(0, 0, 0)
if ans == -1:
    print(-1)
else:
    print(ans + 1)