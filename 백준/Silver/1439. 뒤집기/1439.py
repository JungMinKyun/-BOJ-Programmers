# 백준 1439 뒤집기

s = list(input().strip())

if s[0] == '0':
    cnt_0, cnt_1 = 1, 0
else:
    cnt_0, cnt_1 = 0, 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        continue
    elif s[i] == '0':
        cnt_0 += 1
    else:
        cnt_1 += 1

print(min(cnt_0, cnt_1))
