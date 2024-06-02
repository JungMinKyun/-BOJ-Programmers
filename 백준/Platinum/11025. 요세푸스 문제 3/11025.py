# 백준 11025 요세푸스 문제 3

n, k = map(int, input().split())

trigger = 0
for i in range(n):
    trigger = (trigger + k) % (i+1)

print(trigger+1)