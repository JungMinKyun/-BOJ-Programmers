# 백준 17298 오큰수

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
res = [-1] * n
stack = [0]

for i in range(n):
    while stack and array[i] > array[stack[-1]] and i > stack[-1]:
        res[stack[-1]] = array[i]
        stack.pop()

    stack.append(i)
print(*res)