# 백준 2312 수 복원하기

import sys
input = sys.stdin.readline

lim = 100000
nums = [False,False] + [True]*(lim-1)
primes=[]

for i in range(2, lim + 1):
    if nums[i]:
        primes.append(i)
        for j in range(2*i, lim + 1, i):
            nums[j] = False

for _ in range(int(input())):
    n = int(input())
    ans = {}
    while n > 1 and n not in primes:
        for prime in primes:
            if n > prime and n % prime == 0:
                n = n // prime
                if prime not in ans:
                    ans[prime] = 1
                else:
                    ans[prime] += 1

    if n not in ans:
        ans[n] = 1
    else:
        ans[n] += 1

    for item, key in ans.items():
        print(item, key)