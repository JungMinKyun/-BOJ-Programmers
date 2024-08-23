# 백준 1064 평행사변형 

xa, ya, xb, yb, xc, yc = map(int, input().split())

def distance(x1, y1, x2, y2, x3, y3):
    xd = x1 + x2 - x3
    yd = y1 + y2 - y3
    dist = 0

    for x, y in zip([x1, x2], [y1, y2]):
        dist += ((x - xd)**2 + (y - yd)**2) ** 0.5

    return dist * 2

if (xa-xb) * (yc-yb) == (ya-yb) * (xc-xb):
    print(-1.0)
else:
    dist_list = []

    dist_list.append(distance(xa, ya, xb, yb, xc, yc))
    dist_list.append(distance(xa, ya, xc, yc, xb, yb))
    dist_list.append(distance(xc, yc, xb, yb, xa, ya))

    print(max(dist_list) - min(dist_list))