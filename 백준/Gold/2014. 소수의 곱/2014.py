# 백준 2014 소수의 곱

import sys
import heapq

k, n = map(int, input().split())
primes = list(map(int, input().split()))

heap = []
for prime in primes:
    heapq.heappush(heap, prime)

for i in range(n):
    num = heapq.heappop(heap)
    for prime in primes:
        temp = num * prime
        heapq.heappush(heap, temp)
        if num % prime == 0:
            break

print(num)