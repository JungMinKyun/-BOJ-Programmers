# 백준 17087 숨바꼭질 6

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n, s = map(int, input().split())
array = list(map(int, input().split()))

divisors = []
for elt in array:
    divisors.append(abs(s-elt))

while len(divisors)>=2:
    first = divisors.pop()
    second = divisors.pop()

    divisors.append(gcd(first, second))

print(divisors[0])