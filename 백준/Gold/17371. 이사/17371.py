# 백준 17371 이사

import sys
input = sys.stdin.readline

def sq_dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

minimum = 2e9
x, y = 0, 0

n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]

for x1, y1 in positions:
    maximum = 0
    for x2, y2 in positions:
        temp = sq_dist(x1, y1, x2, y2)
        if temp > maximum:
            maximum = temp
    if maximum < minimum:
        minimum = maximum
        x, y = x1, y1

print(x, y)