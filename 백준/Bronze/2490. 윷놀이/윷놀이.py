# 백준 2490 윷놀이

for _ in range(3):
    a, b, c, d = map(int, input().split())
    result = a + b + c + d

    if result == 0:
        print('D')
    elif result == 1:
        print('C')
    elif result == 2:
        print('B')
    elif result == 3:
        print('A')
    elif result == 4:
        print('E')