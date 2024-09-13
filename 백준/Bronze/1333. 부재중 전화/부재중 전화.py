# 백준 1333 부재중 전화

N, L, D = map(int, input().split())

phone, sing= D, L

for i in range(N):
    if sing-L <= phone < sing:
        while phone < sing:
            phone += D
        sing += L+5
    elif sing <= phone < sing+5:
        break
    else:
        sing += L+5

print(phone)