# 백준 1747 소수 & 팰린드롬

nums = []

for i in range(2, 1004001):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        if str(i) == str(i)[::-1]:
            nums.append(i)

n = int(input())
for num in nums:
    if num >= n:
        print(num)
        break