# 백준 1105 팔

l, r = map(str, input().split())
ans = 0

if len(l) != len(r):
    print(ans)
else:
    for i in range(len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == r[i] == '8':
                ans += 1
    print(ans)