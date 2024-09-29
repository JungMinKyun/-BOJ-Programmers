# 백준 1524 세준세비

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    blank = input()
    n, m = map(int, input().split())
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))

    trigger = max(max(sj), max(sb))
    if trigger in sj:
        print("S")
    else:
        print("B")