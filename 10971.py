# 백준 10971 외판원 순회2

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = []

def BT(start, end, now, cnt):
    if cnt == n:
        if board[now][start] != 0:
            ans.append(end + board[now][start])
        return
    
    for i in range(n):
        if not visited[i] and board[now][i] != 0:
            visited[i] = True
            BT(start, end + board[now][i], i, cnt + 1)
            visited[i] = False
        
for i in range(n):
    visited[i] = True
    BT(i, 0, i, 1)
    visited[i] = False

print(min(ans))