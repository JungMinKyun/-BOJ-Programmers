# 백준 10610 30

n = int(input())
n = sorted(str(n), reverse=True)

if n[-1] != '0' or sum(map(int, n)) % 3 != 0:
    print(-1)
else:
    print(''.join(n))