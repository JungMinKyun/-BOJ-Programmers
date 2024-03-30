# 백준 9613 GCD 합

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    result = 0
    array = list(map(int, input().split()))
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            result += gcd(array[i], array[j])

    print(result)