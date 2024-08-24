# 백준 1159 농구 경기

dictionary = {}

n = int(input())
for _ in range(n):
    temp = str(input())
    if temp[0] not in dictionary:
        dictionary[temp[0]] = 1
    else:
        dictionary[temp[0]] += 1

ans = []
for k, v in dictionary.items():
    if v >= 5:
        ans.append(k)
ans.sort()

if len(ans) == 0: print('PREDAJA')
else: print(''.join(ans))