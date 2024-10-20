# 백준 1975 Number Game

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    cnt = 0
    for i in range(2, num+1):
        temp = num
        while temp:
            if temp % i == 0:
                cnt += 1
                temp //= i
            else:
                break
    print(cnt)