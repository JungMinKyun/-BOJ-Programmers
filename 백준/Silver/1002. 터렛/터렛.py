# 백준 1002 터렛

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    if r1 + r2 > d and abs(r1-r2) < d:
        print(2)
    elif r1 + r2 == d or abs(r1-r2) == d and d != 0:
        print(1)
    elif r1 + r2 < d or abs(r1-r2) > d:
        print(0)
    else:
        print(-1)