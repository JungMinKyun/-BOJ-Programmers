# 백준 1476 날짜 계산

e, s, m = map(int, input().split())
if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0

res = 1
while True:
    if res % 15 == e and res % 28 == s and res % 19 == m:
        break
    res += 1

print(res)