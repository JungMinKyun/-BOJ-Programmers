# 백준 6439 교차

import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

for _ in range(int(input())):
    x1, y1, x2, y2, ax, ay, dx, dy= map(int, input().split())

    if (min(ax, dx) < min(x1, x2) < max(ax, dx)) and (min(ay, dy) < min(y1, y2) < max(ay, dy)) and (min(ax, dx) < max(x1, x2) < max(ax, dx)) and (min(ay, dy) < max(y1, y2) < max(ay, dy)):
        print('T')

    else:
        def check(x1, y1, x2, y2, sx, sy, ex, ey):
            res1 = ccw(x1, y1, x2, y2, sx, sy)
            res2 = ccw(x1, y1, x2, y2, ex, ey)
            res3 = ccw(sx, sy, ex, ey, x1, y1)
            res4 = ccw(sx, sy, ex, ey, x2, y2)

            if res1 * res2 == 0 and res3 * res4 == 0:
                if min(x1, x2) <= max(sx, ex) and min(sx, ex) <= max(x1, x2) and min(y1, y2) <= max(sy, ey) and min(sy, ey) <= max(y1, y2):
                    return 1
                else: 
                    return 0
            elif res1 * res2 <= 0 and res3 * res4 <= 0:
                return 1
            else:
                return 0

        trigger = False
        for sx, sy, ex, ey in [(ax, ay, ax, dy), (ax, ay, dx, ay), (dx, ay, dx, dy), (dx, dy, ax, dy)]:
            if check(x1, y1, x2, y2, sx, sy, ex, ey):
                trigger = True
                break

        if trigger: print('T')
        else: print('F')


