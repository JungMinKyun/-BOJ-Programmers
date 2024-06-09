# 백준 1711 직각삼각형

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x0, y0 = points[i][0], points[i][1]
            x1, y1 = points[j][0], points[j][1]
            x2, y2 = points[k][0], points[k][1]
            a = (x0-x1)**2 + (y0-y1)**2
            b = (x1-x2)**2 + (y1-y2)**2
            c = (x2-x0)**2 + (y2-y0)**2
            
            if a+b+c == max(a, b, c)*2:
                ans += 1
print(ans)