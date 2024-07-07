# 백준 9009 피보나치

import sys
input = sys.stdin.readline

fibo = [1, 1]
while fibo[-1] + fibo[-2] <= 1000000000:
    fibo.append(fibo[-1] + fibo[-2])

for _ in range(int(input())):
    n = int(input())
    ans = []
    while n > 0:
        for i in range(len(fibo)-1, -1, -1):
            if fibo[i] <= n:
                n -= fibo[i]
                ans.append(fibo[i])
                break

    print(*ans[::-1])