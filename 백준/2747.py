# 백준 2747 피보나치 수

n = int(input())
fibo = [0, 1]
for i in range(n):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[n])