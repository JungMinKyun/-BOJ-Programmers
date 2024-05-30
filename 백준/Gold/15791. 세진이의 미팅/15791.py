# 백준 15791 세진이의 미팅

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
mod = 1000000007
factorials = [1] * (n+1)
for i in range(2, n+1):
    factorials[i] = factorials[i-1] * i % mod

def power_(a,b,c):
    if b == 1:
        return a % c
    temp = power_(a, b // 2, c)
    if b % 2 == 0 :
        return temp * temp % c
    else:
        return temp * temp * a % c
    
print(factorials[n] * power_(factorials[k]*factorials[n-k], mod-2, mod) % mod)