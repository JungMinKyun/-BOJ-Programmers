# 백준 5347 LCM

def gcd(a, b):
    return gcd(b, a % b) if b else a

for i in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))