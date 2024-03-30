# 백준 11576 Base Conversion

A, B = map(int, input().split())
M = int(input())
digits = list(map(int, input().split()))

nums = 0
for i in range(M):
    nums += digits[i] * (A ** (M-i-1))

result = []

while nums >= B:
    result.insert(0, nums % B)
    nums = nums // B
result.insert(0, nums)

print(*result)
