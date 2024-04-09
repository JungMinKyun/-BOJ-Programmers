# 백준 3109 빵집

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1]
dy = [1, 1, 1]
ans = 0

def dfs(x, y):
    if y == m - 1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
            board[nx][ny] = 'x'
            if dfs(nx, ny):
                return True
    return False

for i in range(n):
    if dfs(i, 0):
        ans += 1

print(ans)