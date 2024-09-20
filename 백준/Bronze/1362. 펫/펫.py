# 백준 1362 펫

num = 0
while True:
    num += 1
    death = 0
    o, w = map(int, input().split())
    if o == w == 0:
        break

    while True:
        stat, amount = map(str, input().split())
        if stat == '#' and amount == '0':
            break

        if stat == 'E':
            w -= int(amount)
        else:
            w += int(amount)
        if w <= 0:
            death = 1

    if death == 1:
        print(num, 'RIP')
    else:
        if o/2 < w < 2*o:
            print(num, ':-)')
        else:
            print(num, ':-(')