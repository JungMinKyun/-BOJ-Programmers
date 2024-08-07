# 백준 1072 게임

x, y = map(int, input().split())
z = (y*100)//x
left, right, res = 0, x, x

if z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) > z:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)