# 백준 10158 개미

import sys
input = sys.stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

# dx, dy = 1, 1
# for _ in range(t):
#     x += dx
#     y += dy

#     if x == w or x == 0:
#         dx *= -1
#     if y == h or y == 0:
#         dy *= -1

# print(x, y)

temp_x = (x + t) // w
temp_y = (y + t) // h

if temp_x % 2 == 0: sol_x = (x + t) % w
else: sol_x = w - (x + t) % w

if temp_y % 2 == 0: sol_y = (y + t) % h
else: sol_y = h - (y + t) % h

print(sol_x, sol_y)