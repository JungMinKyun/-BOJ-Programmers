# 백준 3474 교수가 된 현우

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0
    while n:
        n //= 5
        result += n
    print(result)