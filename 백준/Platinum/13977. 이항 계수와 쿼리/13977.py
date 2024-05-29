# 백준 13977 이항계수와 쿼리

import sys
input = sys.stdin.readline

mod = 1000000007
factorials = [1] * (4000001)
for i in range(2, 4000001):
    factorials[i] = factorials[i-1] * i % mod

def power_(a,b,c):
    if b == 1:
        return a % c
    temp = power_(a, b // 2, c)
    if b % 2 == 0 :
        return temp * temp % c
    else:
        return temp * temp * a % c
    
for i in range(int(input())):
    n, k = map(int, input().split())
    print(factorials[n] * power_(factorials[k]*factorials[n-k], mod-2, mod) % mod)