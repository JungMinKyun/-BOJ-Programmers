# 백준 1173 운동

n, m, M, T, R = map(int, input().split())

ans, present = 0, m
while n > 0:
    ans += 1
    if present + T <= M:
        present += T
        n -= 1
    else:
        if present == m:
            ans = -1
            break
        else:
            present = max(present - R, m)
            
print(ans)