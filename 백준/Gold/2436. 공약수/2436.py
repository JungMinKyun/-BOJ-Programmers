# 백준 2436 공약수

# gcd 구하기
# lcm // gcd 만들고 제곱근 부터 내려가며 서로소인 지점 찾기

import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

x, y = map(int, input().split())
divisor = y // x

for i in range(int(divisor**0.5), 0, -1):
    j = divisor // i
    r = divisor % i
    if r == 0 and gcd(i, j) == 1:
        print(x*i, x*j)
        break
