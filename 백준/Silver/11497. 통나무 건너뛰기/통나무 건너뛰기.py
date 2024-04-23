# 백준 11497 통나무 건너뛰기

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    logs = sorted(list(map(int, input().split())))
    result = 0
    for i in range(2, n):
        result = max(result, abs(logs[i] - logs[i-2]))
    print(result)