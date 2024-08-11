# 백준 1456 거의 소수

import math

a, b = map(int, input().split())
e = int(b**0.5) + 1

primes = [0, 0] + [1] * (e - 1)
for i in range(2, e+1):
    if primes[i]:
        if i**2 > e:
            break
        for j in range(2*i, e, i):
            primes[j] = 0

ans = 0
for i in range(2, len(primes)):
    if primes[i]:
        temp = i ** 2
        while True:
            if a <= temp <= b:
                ans += 1
            elif temp > b:
                break
            temp *= i
    
print(ans)