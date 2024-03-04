# 백준 16928번 뱀과 사다리 게임

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ladders = [0] * 101
snakes = [0] * 101
visited = [101] * 101

for i in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

for i in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

dx = [1, 2, 3, 4, 5, 6]

Q = deque()
Q.append(1)
visited[1] = 0
while Q:
    x = Q.popleft()
    if x == 100:
        print(visited[100])
        break
    for i in dx:
        nx = x + i
        if nx <= 100 and visited[nx]==101:
            if ladders[nx] != 0:
                nx = ladders[nx]
            if snakes[nx] != 0:
                nx = snakes[nx]
            if visited[nx] == 101:
                visited[nx] = visited[x] + 1
                Q.append(nx)