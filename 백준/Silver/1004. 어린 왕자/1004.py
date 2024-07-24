# 백준 1004 어린왕자

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    ans = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        if (x1-x)**2 + (y1-y)**2 < r**2 and (x2-x)**2 + (y2-y)**2 > r**2:
            ans += 1
        elif (x1-x)**2 + (y1-y)**2 > r**2 and (x2-x)**2 + (y2-y)**2 < r**2:
            ans += 1
    
    print(ans)