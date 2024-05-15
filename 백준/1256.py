# 백준 1256 사전

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
factos = [1] * (n+m+1)
for i in range(2, n+m+1):
    factos[i] = factos[i-1] * i

if factos[n+m] // (factos[n] * factos[m]) < k:
    print(-1)
else:
    result = ''
    while (n > 0 and m > 0) and i > 0:
        if factos[n+m-1] // (factos[n-1] * factos[m]) >= k:
            result += 'a'
            n -= 1
        else:
            result += 'z'
            k -= factos[n+m-1] // (factos[n-1] * factos[m])
            m -= 1
    result += 'a' * n + 'z' * m
    print(result)