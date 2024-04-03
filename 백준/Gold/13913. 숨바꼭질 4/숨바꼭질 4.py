# 백준 13913 숨바꼭질 4

from collections import deque

S, E = map(int, input().split())
N = max(S,E)*2
board = [0] * (N+1)
visited= [0] * (N+1)

Q = deque()
Q.append(S)
board[S]=1
visited[S]=1

while Q:
    x = Q.popleft()
    if x == E:
        print(board[E]-1)
        ans = []
        temp = x
        for _ in range(board[E]):
            ans.append(temp)
            temp = visited[temp]
        print(*ans[::-1])
        break
    for nx in (x-1, x+1, 2*x):
        if 0<=nx<N and board[nx]==0:
            board[nx] = board[x] + 1
            visited[nx] = x
            Q.append(nx)