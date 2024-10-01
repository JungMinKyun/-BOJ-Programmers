# 백준 1568 새

n = int(input())

count, k = 0, 1

while n:
    if k > n:
        k = 1
    n -= k
    k += 1
    count += 1
    
print(count)