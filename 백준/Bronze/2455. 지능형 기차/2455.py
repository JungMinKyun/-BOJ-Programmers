# 백준 2455 지능형 기차

nums, ans = 0, 0
for i in range(4):
    getoff, geton = map(int, input().split())
    nums -= getoff
    nums += geton
    ans = max(ans, nums)

print(ans)