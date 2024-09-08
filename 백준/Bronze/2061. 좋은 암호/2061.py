# 백준 2061 좋은 암호

k, l = map(int, input().split())

trigger = False
for i in range(2, l):
    if k % i == 0:
        trigger = True
        break

if trigger: print('BAD', i)
else: print('GOOD')