# 백준 1681 줄 세우기

n, l = map(int, input().split())

trigger = 1
while n > 0:
    if str(l) not in str(trigger):
        n -= 1
    trigger += 1

print(trigger-1)