# 백준 2437번 저울

import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))

weights.sort()

if weights[0] >= 2:
    print(1)
else:
    total = weights[0]
    for i in range(1, n):
        weight = weights[i]
        if weight <= total + 1:
            total += weight
        else:
            break
    print(total + 1)