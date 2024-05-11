# 백준 11440 피보나치 수의 제곱의 합

import sys
from collections import defaultdict

input = sys.stdin.readline

mod = 1000000007
dp = defaultdict(int)
dp[0] = 0
dp[1] = 1
dp[2] = 1

def fibo(n):
    if not dp[n]:
        if n & 1:
            fn = fibo(n // 2)
            fnp = fibo(n // 2 + 1)
            dp[n] = (fn ** 2 + fnp ** 2) % mod
        else:
            fn = fibo(n // 2)
            fnm = fibo(n // 2 - 1)
            dp[n] = (fn * (fn + 2 * fnm)) % mod
    return dp[n]

n = int(input())
print(fibo(n) * fibo(n+1) % mod)