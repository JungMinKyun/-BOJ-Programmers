# 백준 1019 책 페이지

import sys
input = sys.stdin.readline

n = int(input())
result = [0] * 10
num = 1

def digit_nine(number):
    while number % 10 != 9:
        for i in str(number):
            result[int(i)] += num
        number -= 1
    return number

while n > 0:
    n = digit_nine(n)

    if n < 10:
        for i in range(n + 1):
            result[i] += num
    else:
        for i in range(10):
            result[i] += (n // 10 + 1) * num
    
    n //= 10
    result[0] -= num
    num *= 10
    
print(' '.join(map(str, result)))