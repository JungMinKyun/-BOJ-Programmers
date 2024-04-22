# 백준 16435 스네이크버드

import sys
input = sys.stdin.readline  

n, l = map(int, input().split())
fruits = sorted(list(map(int, input().split())))
for fruit in fruits:
    if l >= fruit:
        l += 1

print(l)