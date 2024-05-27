# 백준 17386 선분 교차 1

import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

res1 = ccw(x1, y1, x2, y2, x3, y3)
res2 = ccw(x1, y1, x2, y2, x4, y4)
res3 = ccw(x3, y3, x4, y4, x1, y1)
res4 = ccw(x3, y3, x4, y4, x2, y2)

if res1 * res2 <= 0 and res3 * res4 <= 0:
    print(1)
else:
    print(0)