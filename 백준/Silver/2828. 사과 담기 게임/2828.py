# 백준 2828 사과 담기 게임

n, m = map(int, input().split())
j = int(input())
now = 1
result = 0

for _ in range(j):
    apple = int(input())
    if now <= apple <= now + m - 1:
        continue
    if apple < now:
        result += now - apple
        now = apple
    else:
        result += apple - (now + m - 1)
        now = apple - m + 1

print(result)