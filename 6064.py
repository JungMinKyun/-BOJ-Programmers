# 백준 6064 카잉 달력

import sys
input = sys.stdin.readline

for i in range(int(input())):
    M, N, x, y = map(int, input().split())
    k = x
    flag = True
    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            print(k)
            flag = False
            break
        k += M
    if flag:
        print(-1)