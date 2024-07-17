# 백준 13458 시험 감독

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for a in A:
    a -= B
    result += 1
    if a > 0:
        result += a // C
        if a % C:
            result += 1

print(result)