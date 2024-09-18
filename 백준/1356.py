# 백준 1356 유진수

num = str(input())
length = len(num)
trigger = False

for i in range(1, length):
    front = num[:i]
    back = num[i:]
    fvalue, bvalue = 1, 1

    for j in front:
        fvalue *= int(j)
    for k in back:
        bvalue *= int(k)

    if fvalue == bvalue:
        trigger = True
        break

if trigger: print('YES')
else: print('NO')