# 백준 3955 캔디 분배

def extenedEulid(n, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, n, b = n//b, b, n%b
        x0, x1 = x1, x0 - q*x1
        y0, y1 = y1, y0 - q*y1
    if n != 1 or x0 > 1e9:
        return 0
    if x0 > 0:
        return x0
    else:
        return x0 + x1

for i in range(int(input())):
    k, c = map(int, input().split())
    if c == 1:
        print(k+1 if k<1e9 else 'IMPOSSIBLE')
    elif k == 1:
        print(1 if c<1e9 else 'IMPOSSIBLE')
    else:
        ans = extenedEulid(c, k)            
        print(ans if ans else 'IMPOSSIBLE')
