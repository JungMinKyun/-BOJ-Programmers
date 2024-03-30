# 백준 6588 골드바흐의 추측

import sys
input = sys.stdin.readline

primes = [0, 0] + [1] * (int(1e6)-1)

for i in range(2, 1001):
    if primes[i]:
        for j in range(i * i, 1000001, i):
            primes[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(3, n, 2):
            if primes[i] and primes[n-i]:
                print("{0} = {1} + {2}".format(n, i, n-i))
                break