# 백준 1016 제곱 ㄴㄴ 수

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = b-a+1
nums = [False] * ans

for i in range(2, int(b**0.5)+1):
    x = i * i
    for j in range(((a-1)//x+1)*x, b+1, x):
        if not nums[j-a]:
            nums[j-a] = True
            ans -= 1

print(ans)