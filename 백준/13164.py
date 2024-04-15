# 백준 13164 행복 유치원

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    kids[i] = kids[i] - kids[i-1]

kids = kids[1:]
kids.sort()
print(sum(kids[:n-k]))