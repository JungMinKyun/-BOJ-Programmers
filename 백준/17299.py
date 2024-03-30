# 백준 17299 오등큰수

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
array = list(map(int, input().split()))
count = Counter(array)

res = [-1] * n
stack = [0]

for i in range(n):
    while stack and count[array[i]] > count[array[stack[-1]]] and i > stack[-1]:
        res[stack[-1]] = array[i]
        stack.pop()

    stack.append(i)

print(*res)