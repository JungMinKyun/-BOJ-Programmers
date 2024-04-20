# 백준 11501 주식

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    max_indx = [0] * n

    for i in range(n-1, -1, -1):
        if i == n-1:
            max_indx[i] = prices[i]
        else:
            max_indx[i] = max(prices[i], max_indx[i+1])

    result = 0
    for i in range(n):
        result += max_indx[i] - prices[i]
    print(result)