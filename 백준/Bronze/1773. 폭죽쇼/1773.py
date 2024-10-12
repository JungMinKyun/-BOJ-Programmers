# 백준 1773 폭죽쇼

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pop_dict = set([])
for _ in range(n):
    pop = int(input())
    cnt = 1
    while pop*cnt <= c:
        pop_dict.add(pop*cnt)
        cnt += 1

print(len(pop_dict))