# 백준 3036 링

import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    g = gcd(rings[0], rings[i])
    print(f'{rings[0]//g}/{rings[i]//g}')