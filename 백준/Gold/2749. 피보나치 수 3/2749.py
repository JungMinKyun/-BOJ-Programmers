# 백준 2749 피보나치 수 3

n = int(input())
mod = 1000000
p = mod//10 * 15

fibo_dict = {0:0, 1:1, 2:1}
for i in range(2, p):
    fibo_dict[i] = (fibo_dict[i-1] + fibo_dict[i-2]) % mod

print(fibo_dict[n%p])