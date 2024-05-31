# 백준 11402 이항 계수 4

import sys
input = sys.stdin.readline

def lucas(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    x = 1
    for i in range(1, k+1):
        x *= (n-i+1)
        x //= i
    return x

n, k, m = map(int, input().split())
n_list, m_list = [], []
while n or k:
    n_list.append(n%m)
    m_list.append(k%m)
    n //= m
    k //= m

result = 1
for i in range(len(n_list)):
    result *= lucas(n_list[i], m_list[i])
    result %= m
print(result)