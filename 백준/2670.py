# 백준 2670 연속부분최대곱

nums = []
n = int(input())
nums = list(float(input()) for _ in range(n))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] * nums[i-1])
print('%0.3f' % max(nums))