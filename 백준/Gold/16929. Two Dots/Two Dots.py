# 백준 16929 Two Dots

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[x][y]:
            if visited[nx][ny] != 0:
                if visited[x][y] - visited[nx][ny] >= 3:
                    print('Yes')
                    sys.exit()
                continue
            else:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny)
                visited[nx][ny] = 0

for i in range(n):
    for j in range(m): 
        visited[i][j] = 1
        dfs(i, j)
        visited[i][j] = 0

print('No')