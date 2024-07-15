# 백준 4104 크냐?

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a > b: print('Yes')
    else: print('No')