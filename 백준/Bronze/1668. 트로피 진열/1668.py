# 백준 1668 트로피 진열

n = int(input())
trophy = [int(input()) for _ in range(n)]

left, right = 0, 0
left_max, right_max = 0, 0

for i in range(n):
    if trophy[i] > left_max:
        left += 1
        left_max = trophy[i]
    if trophy[-(i+1)] > right_max:
        right += 1
        right_max = trophy[-(i+1)]

print(left)
print(right)