# 백준 1418 K-세준수\

n = int(input())
k = int(input())

nums = [False,False] + [True]*(n-1)
primes=[1]

for i in range(2, n + 1):
    if nums[i]:
        primes.append(i)
        for j in range(2*i, n + 1, i):
            nums[j] = False

knums = [1] * (n+1)
for i in range(2, n+1):
    if nums[i] and i > k:
        for j in range(i, n+1, i):
            knums[j] = 0

print(sum(knums)-1)