# 백준 2622 삼각형 만들기

length = int(input())

ans = 0
for s in range(1, length+1):
    for m in range(s, length+1):
        l = length - s - m
        if l < s + m:
            if m > l:
                break
            ans += 1

print(ans)