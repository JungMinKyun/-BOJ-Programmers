# 백준 15824 너 봄에는 캡사이신이 맛있단다

import sys
input = sys.stdin.readline

n = int(input())
menus = list(map(int, input().split()))
menus.sort()

mod = 1000000007
twos = [1] * (n+1)
for i in range(1, n+1):
    twos[i] = twos[i-1] * 2 % mod

result = 0 
for i in range(n):
    for j in range(n-1, i, -1):
        value = menus[j] - menus[i]
        value *= twos[j-i-1]
        result += value % mod

print(result % mod)
