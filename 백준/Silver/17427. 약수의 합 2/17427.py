# 백준 17427 약수의 합 2

n = int(input())
res = 0

for i in range(1, n+1):
    res += i * (n//i)
    
print(res)