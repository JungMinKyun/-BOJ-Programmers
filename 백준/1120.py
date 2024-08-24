# 백준 1120 문자열

sub, full = map(str, input().split())

ans = 51
for i in range(len(full) - len(sub) + 1):
    cnt = 0
    for j in range(len(sub)):
        if sub[j] != full[j+i]:
            cnt += 1

    ans = min(ans, cnt)

print(ans)