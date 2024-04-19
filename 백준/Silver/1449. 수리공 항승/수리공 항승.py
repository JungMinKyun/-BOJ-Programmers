# 백준 1449 수리공 항승

n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()

res = 1
init = holes[0]
for hole in holes:
    if hole > init + l - 1:
        init = hole
        res += 1

print(res)