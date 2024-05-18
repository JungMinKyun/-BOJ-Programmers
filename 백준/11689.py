# 백준 11689 GCD(n, k) = 1

import sys
import math
input = sys.stdin.readline

n = int(input())

res = n
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        res *= (1-1/i)
            
if n != 1:
    res *= (1-1/n)

print(int(res))