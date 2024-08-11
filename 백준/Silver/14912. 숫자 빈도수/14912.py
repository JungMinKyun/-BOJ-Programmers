# 백준 14912 숫자 빈도수

n, d = map(int, input().split())

ans = 0 
for i in range(1, n+1):
    string = str(i)
    for elt in string:
        if elt == str(d):
            ans += 1

print(ans)