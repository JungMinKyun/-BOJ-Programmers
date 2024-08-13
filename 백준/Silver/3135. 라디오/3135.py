#  백준 3135 라디오

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
channels = [int(input()) for _ in range(int(input()))]

channels.sort()
ans = abs(b-a)

for chan in channels:
    ans = min(ans, abs(b-chan)+1)

print(ans)