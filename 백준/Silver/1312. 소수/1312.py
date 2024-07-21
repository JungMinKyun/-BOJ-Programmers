# 백준 1312 소수

a, b, n = map(int, input().split())
print((a * (10 ** n) // b)%10)