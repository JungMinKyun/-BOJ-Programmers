# 백준 1744번 수 묶기

import sys
input = sys.stdin.readline

n = int(input())
posit = []
negat = []
one = []
zero = []

for _ in range(n):
    num = int(input())
    if num > 1:
        posit.append(num)
    elif num < 0:
        negat.append(num)
    elif num == 1:
        one.append(num)
    else:
        zero.append(num)

posit.sort(reverse=True)
negat.sort()

ans = 0

while len(posit) > 1:
    temp = 1
    for _ in range(2):
        temp *= posit.pop(0)
    ans += temp

if posit:
    ans += posit[0]

while len(negat) > 1:
    temp = 1
    for _ in range(2):
        temp *= negat.pop(0)
    ans += temp

if not zero and negat:
    ans += negat[0]

ans += len(one)

print(ans)