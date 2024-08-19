# 백준 1032 명령 프롬프트

n = int(input())
start = list(str(input()))

for _ in range(n-1):
    cmp = list(str(input()))

    for i in range(len(cmp)):
        if start[i] != cmp[i]:
            start[i] = '?'

print(''.join(start))
