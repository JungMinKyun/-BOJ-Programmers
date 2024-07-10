# 백준 2018 수들의 합 5

import sys
input = sys.stdin.readline
n = int(input())
start, end, total, count = 1, 1, 1, 1

if n <= 2:
    pass
else:
    while end < n//2 + 2:
        if total == n:
            count += 1
            end += 1
            total += end
        elif total < n:
            end += 1
            total += end
        else:
            total -= start
            start += 1

print(count)