# 백준 15824 너 봄에는 캡사이신이 맛있단다

import sys
input = sys.stdin.readline

mod = 1000000007

def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    half = pow(a, b//2)
    return half * half % mod if b % 2 == 0 else half * half * a % mod

n = int(input())
menus = list(map(int, input().split()))
menus.sort()

result = 0 
for i in range(n):
    result += menus[i] * (pow(2, i) - pow(2, n-i-1))

print(result % mod)
