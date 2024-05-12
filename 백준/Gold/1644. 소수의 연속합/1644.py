# 백준 1644 소수의 연속합

import sys
input = sys.stdin.readline

n = int(input())

primes = []
is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[0] = False

for i in range(2, n+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            is_prime[j] = False

cnt, first, last = 0, 0, 0
while last <= len(primes):
    if sum(primes[first:last]) < n:
        last += 1
    elif sum(primes[first:last]) > n:
        first += 1
    else:
        cnt += 1
        last += 1

print(cnt)