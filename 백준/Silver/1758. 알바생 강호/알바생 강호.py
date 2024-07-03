# 백준 1758 알바생 강호

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

ans = 0
for i in range(n):
    if nums[i] - i >= 0:
        ans += (nums[i] - i)

print(ans)