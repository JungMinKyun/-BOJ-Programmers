# 백준 14226 이모티콘

from collections import deque
n = int(input())

dp = [[0] * 1001 for _ in range(1001)]

Q = deque()
Q.append((1, 0))
while Q:
    x, board = Q.popleft()
    if x == n:
          print(dp[x][board])
          break
    for nx, nboard in [(x, x), (x+board, board), (x-1, board)]:
        if 0 <= nx < 1001 and 0 <= nboard < 1001 and not dp[nx][nboard]:
            dp[nx][nboard] = dp[x][board] + 1
            Q.append((nx, nboard))