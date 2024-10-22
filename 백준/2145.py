# 백준 2145 숫자 놀이

while True:
    n = input()
    if n == '0':
        break
    while len(n) > 1:
        n = str(sum(map(int, n)))
    print(n)