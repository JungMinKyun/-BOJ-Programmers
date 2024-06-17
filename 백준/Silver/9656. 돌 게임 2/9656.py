# 백준 9656 돌 게임 2

n = int(input())
if n % 4 == 1 or n % 4 == 3:
    print('CY')
else:
    print('SK')