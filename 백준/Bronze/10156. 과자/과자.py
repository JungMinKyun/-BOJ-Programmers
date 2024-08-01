k, n, m = map(int, input().split())
target = k*n

if target >= m: print(target - m)
else: print(0)