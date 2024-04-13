# 백준 1052 물

n, m = map(int, input().split())

cnt = n
while True:
    trigger = bin(cnt).count('1')
    if trigger <= m:
        print(cnt - n)
        break
    cnt += 1