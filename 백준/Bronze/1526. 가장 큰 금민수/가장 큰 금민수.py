# 백준 1526 가장 큰 금민수

n = int(input())
while True:
    if all(i in ['4', '7'] for i in str(n)):
        print(n)
        break
    n -= 1