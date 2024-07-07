# 백준 9375 패션왕 신해빈

for _ in range(int(input())):
    clothes = {}
    for i in range(int(input())):
        what, kind = map(str, input().split())
        if kind not in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1

    ans = 1
    for value in clothes.values():
        ans *= (value + 1)
        
    print(ans-1)