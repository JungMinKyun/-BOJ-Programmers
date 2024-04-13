# 백준 2217 로프

import sys
input = sys.stdin.readline 

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

ans = 0
for i in range(n):
    ans = max(ans, ropes[i] * (n-i))

print(ans)
