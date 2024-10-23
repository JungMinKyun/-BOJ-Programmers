# 백준 2460 지능형 기차 2

import sys
input = sys.stdin.readline

ans = 0
now = 0
for _ in range(10):
    out, come = map(int, input().split())
    now = now - out + come
    ans = max(ans, now)
print(ans)