# 백준 1964 오각형, 오각형, 오각형...

n = int(input())
result = 5
for i in range(n-1):
    result += 3 * (i+2) + 1
    result %= 45678

print(result)