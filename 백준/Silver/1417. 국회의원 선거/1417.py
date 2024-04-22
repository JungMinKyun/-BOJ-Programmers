# 백준 1417 국회의원 선거

import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    first = int(input())
    elect = [int(input()) for _ in range(n-1)]

    ans = 0
    while True:
        if first <= max(elect):
            first += 1
            ans += 1
            elect[elect.index(max(elect))] -= 1
        else:
            break

    print(ans)