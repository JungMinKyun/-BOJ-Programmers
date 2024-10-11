# 백준 2028 자기복제수

n = int(input())
for _ in range(n):
    num = int(input())
    deg = len(str(num))

    if num ** 2 % (10 ** deg) == num:
        print('YES')
    else:
        print('NO')