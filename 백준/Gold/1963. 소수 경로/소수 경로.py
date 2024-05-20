# 백준 1963  소수 경로

import sys
from collections import deque
input = sys.stdin.readline

is_prime = [1] * 10000
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, 10000):
    if is_prime[i]:
        for j in range(i*2, 10000, i):
            is_prime[j] = 0

primes = []
for i in range(10000):
    if is_prime[i] and i >= 1000:
        primes.append(i)
prime = set(primes)

for i in range(int(input())):
    a, b = map(int, input().split())
    visited = [0] * 10000
    visited[a] = 1

    Q = deque()
    Q.append((a, 0))
    while Q:
        out, count = Q.popleft()
        if out == b:
            print(count)
            break
        for i in range(4):
            for j in range(10):
                temp = list(str(out))
                temp[i] = str(j)
                temp = int(''.join(temp))
                if 1000 <= temp and not visited[temp] and temp in prime:
                    visited[temp] = 1
                    Q.append((temp, count+1))