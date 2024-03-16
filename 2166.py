# 백준 2166 다각형의 면적

import sys
input = sys.stdin.readline

n = int(input())
x_points = []
y_points = []
for _ in range(n):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)
x_points.append(x_points[0]) 
y_points.append(y_points[0])

result_x = 0
result_y = 0
for i in range(n):
    result_x += x_points[i] * y_points[i+1]
    result_y += y_points[i] * x_points[i+1]

print(round(abs(result_x - result_y) / 2, 1))